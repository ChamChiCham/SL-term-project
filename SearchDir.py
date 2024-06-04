import fileDuplicator

class searchDir:
    history = []
    history_file = fileDuplicator
    flag = 0
    def __init__(self, char_name):
        file_obj = open("user_name.txt",'a')
        file_obj.close()
        self.history = self.history_file.fileDuplicator().getHistory()
        file_obj = open("user_name.txt",'a')
        if len(self.history) == 0:
            file_obj.write(char_name + '\n')
        else:
            for i in self.history:
                if char_name + '\n' == i:
                    self.flag = 1
                    break

            if self.flag == 0:
                file_obj.write(char_name + '\n')

        file_obj.close()

###########################################################################
#파일에 유저 검색 기록 등록하는 방법

#test = searchDir("넹븝sdsad")

###########################################################################
#print(fileDuplicator.fileDuplicator().getHistory())
#   이런 식으로 메모장만 읽어올 수 있음 참고로 개행문자까지 검사해야 같은지 확인할 수 있음
#   모르겠으면 16번째 줄 함 보삼
#   이름 받은거 searchDir로 입력하고 검색기록 나오는 곳에는 getHistory사용해서 하면 될듯?
###########################################################################