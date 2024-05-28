from tkinter import *
from tkinter import font
from winsound import *

from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk

import APIprocess

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

SEARCH_ENTRY_X = 300
SEARCH_ENTRY_Y = 100

SEARCH_ITEM_SIZE = 10

SEARCH_ITEM1_X = 350
SEARCH_ITEM2_X = 700
SEARCH_ITEM_Y = 125
SEARCH_ITEM_DIFF = 120


class mainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("1280x960")
        self.window.configure(bg="green")

        self.font_option = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_entry = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_item = font.Font(self.window, size=16, family='맑은 고딕')

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

        self.objects = []
        self.window.mainloop()

    def clear_objects(self):
        for o in self.objects:
            o.destroy()
        self.objects = []


    def option_search_func(self):
        self.clear_objects()

        # create entry and button
        self.entry = Entry(self.window, font=self.font_search_entry)
        self.entry.place(x=500, y=50)

        self.entry_button = Button(self.window, width=10, height=5, command=self.option_search_button_func)
        self.entry_button.place(x=850, y=30)

        self.objects.append(self.entry)
        self.objects.append(self.entry_button)

        # create item button
        self.item = []
        for i in range(7):
            self.item.append(Label(self.window, width=8, height=4))
            self.item[-1].place(x=SEARCH_ITEM1_X, y=SEARCH_ITEM_Y + i * SEARCH_ITEM_DIFF)
            self.objects.append(self.item[-1])

        for i in range(6):
            self.item.append(Label(self.window, width=8, height=4))
            self.item[-1].place(x=SEARCH_ITEM2_X, y=SEARCH_ITEM_Y + i * SEARCH_ITEM_DIFF)
            self.objects.append(self.item[-1])

    def option_search_button_func(self):
        name = str(self.entry.get())
        if not name:
            return

        self._make_item(name)


    def _make_item_image(self, image, idx, x, y):
        with urllib.request.urlopen(image) as u:
             raw_data=u.read()
        im=Image.open(BytesIO(raw_data))
        self.image.append(ImageTk.PhotoImage(im))
        self.item[idx].destroy()
        self.item[idx] = Button(self.window, width=64, height=64, image=self.image[-1])
        self.item[idx].place(x=x, y=y)

    def _make_item(self, name):
        self.player = []
        self.image = []
        new_API = APIprocess.Get_char_json(name)
        new_API.getAmorizes()
        global cnt
        cnt = 0

        def make_item_each(func, x, y):
            global cnt
            self.player.append(func())
            self._make_item_image(self.player[cnt][0], cnt, x, y)
            cnt += 1

        make_item_each(new_API.GetplayerWeaponinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y)
        make_item_each(new_API.GetplayerHeadinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 1 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerTopinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 2 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerUnderinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 3 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerHandsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 4 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerPauldronsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 5 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerBraceletinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 6 * SEARCH_ITEM_DIFF)
        
        make_item_each(new_API.GetplayerNecklessinfo,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y)
        make_item_each(new_API.GetplayerEarRing1info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 1 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerEarRing2info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 2 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerRing1info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 3 * SEARCH_ITEM_DIFF)
        make_item_each(new_API.GetplayerRing2info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 4 * SEARCH_ITEM_DIFF)
        # make_item_each(new_API.GetplayerStoneinfo,\
        #                SEARCH_ITEM2_X, SEARCH_ITEM_Y + 5 * SEARCH_ITEM_DIFF)

    def option_goal_func(self):
        self.clear_objects()


    def option_todo_func(self):
        self.clear_objects()


    def option_history_func(self):
        self.clear_objects()

    def option_popup_func(self):
        self.clear_objects()


        
