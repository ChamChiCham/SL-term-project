//DESKTOP-O6QFSN0\SQLEXPRESS

// SQLConnect_ref.cpp  
// compile with: odbc32.lib  
#include <iostream>
#include <vector>
#include <locale>
#include <unordered_map>
#include <string>
#include <codecvt>
#include <format>
#include <atlconv.h>



#include <WS2tcpip.h>
#include <MSWSock.h>

#pragma comment(lib, "WS2_32.lib")
#pragma comment(lib, "MSWSock.lib")

#include <windows.h>  
#include <sqlext.h>

SQLHENV henv;
SQLHDBC hdbc;
SQLHSTMT hstmt;

/************************************************************************
/* HandleDiagnosticRecord : display error/warning information
/*
/* Parameters:
/*     hHandle    ODBC handle
/*     hType      Type of handle (SQL_HANDLE_STMT, SQL_HANDLE_ENV, SQL_HANDLE_DBC)
/*     RetCode    Return code of failing command
/************************************************************************/
void display_error(SQLHANDLE hHandle, SQLSMALLINT hType, RETCODE RetCode)
{
	SQLSMALLINT iRec = 0;
	SQLINTEGER  iError;
	WCHAR      wszMessage[1000];
	WCHAR      wszState[SQL_SQLSTATE_SIZE + 1];
	if (RetCode == SQL_INVALID_HANDLE) {
		fwprintf(stderr, L"Invalid handle!\n");
		return;
	}
	while (SQLGetDiagRec(hType, hHandle, ++iRec, wszState, &iError, wszMessage,
		(SQLSMALLINT)(sizeof(wszMessage) / sizeof(WCHAR)), (SQLSMALLINT*)NULL) == SQL_SUCCESS) {
		// Hide data truncated..
		if (wcsncmp(wszState, L"01004", 5)) {
			fwprintf(stderr, L"[%5.5s] %s (%d)\n", wszState, wszMessage, iError);
		}
	}
}


bool connect_database()
{
    SQLRETURN retcode;


    // Allocate environment handle  
    retcode = SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);
    setlocale(LC_ALL, "korean");

    // Set the ODBC version environment attribute  
    if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
        retcode = SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (void*)SQL_OV_ODBC3, 0);

        // Allocate connection handle  
        if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
            retcode = SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);

            // Set login timeout to 5 seconds  
            if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
                SQLSetConnectAttr(hdbc, SQL_LOGIN_TIMEOUT, (SQLPOINTER)5, 0);

                // Connect to data source  
                retcode = SQLConnect(hdbc, (SQLWCHAR*)L"SL_DB", SQL_NTS, (SQLWCHAR*)NULL, 0, NULL, 0);

                // Allocate statement handle  
                if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
                   
					std::cout << "Database Connected" << std::endl;
					return true;
                }
				SQLDisconnect(hdbc);
            }
			SQLFreeHandle(SQL_HANDLE_DBC, hdbc);
        }
        SQLFreeHandle(SQL_HANDLE_ENV, henv);
    }
    return false;
}

void disconnect_database()
{
    SQLDisconnect(hdbc);
    SQLFreeHandle(SQL_HANDLE_DBC, hdbc);
    SQLFreeHandle(SQL_HANDLE_ENV, henv);
}

//=================
constexpr int PORT_NUM = 4000;
constexpr int BUF_SIZE = 512;
constexpr int NAME_SIZE = 36;

constexpr char CS_WRITE = 0;
constexpr char CS_READ = 1;
constexpr char SC_GIVE = 2;

#pragma pack (push, 1)
struct CS_WRITE_PACKET {
	unsigned char size;
	char	type;
	char	name[NAME_SIZE];
	float	level;
};

struct CS_READ_PACKET {
	unsigned char size;
	char	type;
};

struct SC_GIVE_PACKET {
	unsigned char size;
	char	type;
	char	name[10][NAME_SIZE];
};
#pragma pack (pop)

enum COMP_TYPE { OP_ACCEPT, OP_RECV, OP_SEND };

class OVER_EXP {
public:
    WSAOVERLAPPED _over;
    WSABUF _wsabuf;
    char _send_buf[BUF_SIZE];
    COMP_TYPE _comp_type;
    OVER_EXP()
    {
        _wsabuf.len = BUF_SIZE;
        _wsabuf.buf = _send_buf;
        _comp_type = OP_RECV;
        ZeroMemory(&_over, sizeof(_over));
    }
    OVER_EXP(char* packet)
    {
        _wsabuf.len = packet[0];
        _wsabuf.buf = _send_buf;
        ZeroMemory(&_over, sizeof(_over));
        _comp_type = OP_SEND;
        memcpy(_send_buf, packet, packet[0]);
    }
};
class SESSION {
	OVER_EXP _recv_over;

public:
	// 객체 정보
	size_t	    _id;
	SOCKET		_socket;

	// 패킷 재조립을 위한 남은 데이터 수 저장
	int			_prev_remain;

public:
	SESSION()
	{
		_id = -1;
		_socket = 0;
		_prev_remain = 0;
	}

	~SESSION() {}

	void do_recv()
	{
		DWORD recv_flag = 0;
		memset(&_recv_over._over, 0, sizeof(_recv_over._over));
		_recv_over._wsabuf.len = BUF_SIZE - _prev_remain;
		_recv_over._wsabuf.buf = _recv_over._send_buf + _prev_remain;
		WSARecv(_socket, &_recv_over._wsabuf, 1, 0, &recv_flag,
			&_recv_over._over, 0);
	}

	void do_send(void* packet)
	{
		OVER_EXP* sdata = new OVER_EXP{ reinterpret_cast<char*>(packet) };
		WSASend(_socket, &sdata->_wsabuf, 1, 0, 0, &sdata->_over, 0);
	}
};

std::unordered_map<size_t, SESSION> clients;

HANDLE h_iocp;
SOCKET g_s_socket;
SOCKET g_c_socket;
OVER_EXP g_a_over;

size_t g_id = 0;

//=================


void disconnect(size_t c_id)
{
	closesocket(clients[c_id]._socket);
	clients.erase(c_id);
}

void process_packet(size_t c_id, char* packet)
{
	switch (packet[1]) {
	case CS_WRITE: {
		std::cout << "cs_write" << std::endl;
		CS_WRITE_PACKET* p = reinterpret_cast<CS_WRITE_PACKET*>(packet);
		
		std::string str{ p->name };
		USES_CONVERSION;
		std::wstring wstr = std::wstring(A2W(str.c_str()));

		std::wstring exec{std::format(L"EXEC update_user @Param1 = '{}', @Param2 = {}", wstr, p->level)};
		std::wcout << exec << std::endl;


		int retcode = SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);
		if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
			// SQL 문장 실행
			retcode = SQLExecDirect(hstmt, (SQLWCHAR*)exec.c_str(), SQL_NTS);
			if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
				std::cout << "Data inserted successfully." << std::endl;
			}
			else {
				std::cout << "Failed to insert data." << std::endl;
				display_error(hstmt, SQL_HANDLE_STMT, retcode);
			}
			// statement 핸들 해제
			SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
		}
		else {
			std::cout << "Failed to allocate a statement handle." << std::endl;
		}
		break;
	}
	case CS_READ: {
		std::cout << "cs_read" << std::endl;

		int retcode = SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);
		if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {

			SQLVARCHAR name[NAME_SIZE]{};
			SQLREAL level{};
			std::string read_names[10];

			// SQL 문장 실행
			retcode = SQLExecDirect(hstmt, (SQLWCHAR*)L"EXEC get_user", SQL_NTS);
			if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
				std::cout << "Data Select successfully." << std::endl;
				SQLLEN cbName = 0, cbLevel = 0;
				retcode = SQLBindCol(hstmt, 1, SQL_C_CHAR, name, 36, &cbName);
				retcode = SQLBindCol(hstmt, 2, SQL_C_FLOAT, &level, 20, &cbName);
				int idx = 0;
				while (true)
				{
					retcode = SQLFetch(hstmt);

					if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO)
					{
						std::cout << name << '\t' << level << std::endl;
						read_names[idx++] = reinterpret_cast<char*>(name);
					}

					else if (retcode == SQL_ERROR || retcode == SQL_SUCCESS_WITH_INFO)
					{
						display_error(hstmt, SQL_HANDLE_STMT, retcode);
						break;
					}

					else if (retcode == SQL_NO_DATA)
					{
						SQLCloseCursor(hstmt);
						break;
					}
				}
			}
			else {
				std::cout << "Failed to select data." << std::endl;
				display_error(hstmt, SQL_HANDLE_STMT, retcode);
			}
			// statement 핸들 해제
			SQLFreeHandle(SQL_HANDLE_STMT, hstmt);

			SC_GIVE_PACKET rp;
			rp.type = SC_GIVE;
			rp.size = sizeof(rp);
			for (int i = 0; i < 10; ++i) {
				strcpy_s(rp.name[i], NAME_SIZE, read_names[i].c_str());
			}
			clients[c_id].do_send(&rp);
		}
		else {
			std::cout << "Failed to allocate a statement handle." << std::endl;
		}

		break;
	}
	}
}

int main()
{
    if (not connect_database()) {
        exit(-1);
    }

    WSADATA WSAData;
    WSAStartup(MAKEWORD(2, 2), &WSAData);
    g_s_socket = WSASocket(AF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
    SOCKADDR_IN server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT_NUM);
    server_addr.sin_addr.S_un.S_addr = INADDR_ANY;
    bind(g_s_socket, reinterpret_cast<sockaddr*>(&server_addr), sizeof(server_addr));
    listen(g_s_socket, SOMAXCONN);
    SOCKADDR_IN cl_addr;
    int addr_size = sizeof(cl_addr);


	// iocp 객체 생성
	h_iocp = CreateIoCompletionPort(INVALID_HANDLE_VALUE, 0, 0, 0);

	// 서버 소켓에 연결
	CreateIoCompletionPort(reinterpret_cast<HANDLE>(g_s_socket), h_iocp, 9999, 0);

	// Accept를 위한 클라이언트 소켓 하나 생성. 
	g_c_socket = WSASocket(AF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
	g_a_over._comp_type = OP_ACCEPT;

	// 비동기 Accept
	AcceptEx(g_s_socket, g_c_socket, g_a_over._send_buf, 0, addr_size + 16, addr_size + 16, 0, &g_a_over._over);


	while (true) {
		DWORD num_bytes;
		ULONG_PTR key;
		WSAOVERLAPPED* over = nullptr;
		BOOL ret = GetQueuedCompletionStatus(h_iocp, &num_bytes, &key, &over, INFINITE);
		OVER_EXP* ex_over = reinterpret_cast<OVER_EXP*>(over);
		if (FALSE == ret) {
			if (ex_over->_comp_type == OP_ACCEPT) std::cout << "Accept Error";
			else {
				std::cout << "GQCS Error on client[" << key << "]\n";
				disconnect(key);
				if (ex_over->_comp_type == OP_SEND) delete ex_over;
				continue;
			}
		}

		if ((0 == num_bytes) && ((ex_over->_comp_type == OP_RECV) || (ex_over->_comp_type == OP_SEND))) {
			disconnect(key);
			if (ex_over->_comp_type == OP_SEND) delete ex_over;
			continue;
		}

		switch (ex_over->_comp_type) {
		case OP_ACCEPT: {
			size_t client_id = g_id++;
			CreateIoCompletionPort(reinterpret_cast<HANDLE>(g_c_socket), h_iocp, client_id, 0);

			clients.insert(std::make_pair(client_id, SESSION{}));
			clients[client_id]._socket = g_c_socket;
			clients[client_id]._id = client_id;
			clients[client_id].do_recv();

			g_c_socket = WSASocket(AF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
			ZeroMemory(&g_a_over._over, sizeof(g_a_over._over));
			AcceptEx(g_s_socket, g_c_socket, g_a_over._send_buf, 0, addr_size + 16, addr_size + 16, 0, &g_a_over._over);
			break;
		}
		case OP_RECV: {
			int remain_data = num_bytes + clients[key]._prev_remain;
			char* p = ex_over->_send_buf;
			while (remain_data > 0) {
				int packet_size = p[0];
				if (packet_size <= remain_data) {
					process_packet(key, p);
					p = p + packet_size;
					remain_data = remain_data - packet_size;
				}
				else break;
			}
			clients[key]._prev_remain = remain_data;
			if (remain_data > 0) {
				memcpy(ex_over->_send_buf, p, remain_data);
			}
			clients[key].do_recv();
			break;
		}
		case OP_SEND:
			delete ex_over;
			break;
		}
	}
	closesocket(g_s_socket);
	WSACleanup();

    disconnect_database();
}