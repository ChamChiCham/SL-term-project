from tkinter import *
from tkinter import font
from winsound import *

OPTION1_X = 50
OPTION2_X = OPTION1_X
OPTION3_X = OPTION1_X
OPTION4_X = OPTION1_X
OPTION5_X = OPTION1_X

OPTION_Y_DIFF = 150
OPTION1_Y = 100
OPTION2_Y = OPTION1_Y + OPTION_Y_DIFF
OPTION3_Y = OPTION2_Y + OPTION_Y_DIFF
OPTION4_Y = OPTION3_Y + OPTION_Y_DIFF
OPTION5_Y = OPTION4_Y + OPTION_Y_DIFF

OPTION_SIZE_X = 10
OPTION_SIZE_Y = 3



class mainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("1280x960")
        self.window.configure(bg="green")

        self.font_option = font.Font(self.window, size=16, family='맑은 고딕')

        # place option
        self.option_search = Button(self.window, text="유저 검색",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_search_func)
        self.option_search.place(x=OPTION1_X,y=OPTION1_Y)

        self.option_goal = Button(self.window,text="목표치 설정", \
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_goal_func)
        self.option_goal.place(x=OPTION2_X,y=OPTION2_Y)

        self.option_todo = Button(self.window,text="내 할일",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_todo_func)
        self.option_todo.place(x=OPTION3_X,y=OPTION3_Y)

        self.option_history = Button(self.window,text="검색 기록", \
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_history_func)
        self.option_history.place(x=OPTION4_X,y=OPTION4_Y)

        self.option_popup = Button(self.window,text="팝업 스토어",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_popup_func)
        self.option_popup.place(x=OPTION5_X,y=OPTION5_Y)

        self.window.mainloop()

    def option_search_func(self):
        pass

    def option_goal_func(self):
        pass


    def option_todo_func(self):
        pass


    def option_history_func(self):
        pass

    def option_popup_func(self):
        pass


        
