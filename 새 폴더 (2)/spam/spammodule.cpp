#include "python.h"

#include <iostream>

#include <WS2tcpip.h>
#include <MSWSock.h>

#pragma comment(lib, "WS2_32.lib")
#pragma comment(lib, "MSWSock.lib")

#include <windows.h>  
#include <sqlext.h>

constexpr int PORT_NUM = 4000;
constexpr int BUF_SIZE = 512;
constexpr int NAME_SIZE = 36;

constexpr char CS_WRITE = 0;
constexpr char CS_READ = 1;
constexpr char SC_GIVE = 2;
constexpr const char* SERVER_ADDR = "127.0.0.1";

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
public:
	OVER_EXP	_recv_over;
	size_t	    _id;
	SOCKET		_socket;

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
		WSARecv(_socket, &_recv_over._wsabuf, 1, 0, &recv_flag, 0, 0);
	}

	void do_send(void* packet)
	{
		OVER_EXP* sdata = new OVER_EXP{ reinterpret_cast<char*>(packet) };
		WSASend(_socket, &sdata->_wsabuf, 1, 0, 0, &sdata->_over, 0);
	}
};

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

SESSION session;

void init()
{
	std::wcout.imbue(std::locale("korean"));
	WSADATA WSAData;
	WSAStartup(MAKEWORD(2, 0), &WSAData);
	SOCKET s_socket = WSASocket(AF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
	SOCKADDR_IN server_addr;
	ZeroMemory(&server_addr, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(PORT_NUM);
	inet_pton(AF_INET, SERVER_ADDR, &server_addr.sin_addr);
	connect(s_socket, reinterpret_cast<sockaddr*>(&server_addr), sizeof(server_addr));
	session._socket = s_socket;

}

static PyObject *

write_name(PyObject *self, PyObject *args)
{
	init();
	CS_WRITE_PACKET p;
	p.type = CS_WRITE;
	p.size = sizeof(p);
	strcpy_s(p.name, NAME_SIZE, "TKadkcl2");
	p.level = 1540.f;
	session.do_send(&p);

	closesocket(session._socket);
	WSACleanup();

	return Py_BuildValue("b", len);
}

static PyObject*

get_name(PyObject* self, PyObject* args)
{
	init();
}

static PyMethodDef SpamMethods[] = {
	{ "write", write_name, METH_VARARGS,
	"count a string length." },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static PyMethodDef SpamMethods1[] = {
	{ "get", get_name, METH_VARARGS,
	"count a string length." },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // 모듈 이름
	"It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
