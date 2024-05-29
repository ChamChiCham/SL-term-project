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


SEARCH_ITEM1_X = 350
SEARCH_ITEM2_X = 800
SEARCH_ITEM_Y = 140
SEARCH_ITEM_DIFF = 120


class mainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("너, 로아 열심히 하고 있니?")
        self.window.geometry("1280x960")
        self.window.configure(bg="green")

        self.font_option = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_entry = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_item_name = font.Font(self.window, size=14, family='맑은 고딕')

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
        self.option = "None"
        self.window.mainloop()

    def clear_objects(self):
        match self.option:
            case "Search":
                self.entry.destroy()
                self.entry_button.destroy()
                self._delete_item()
            case _:
                pass

    def option_search_func(self):

        # clear objects
        self.clear_objects()
        self.option = "Search"

        # create entry and button
        self.entry = Entry(self.window, font=self.font_search_entry)
        self.entry.place(x=500, y=50)

        self.entry_button = Button(self.window, width=10, height=5, command=self.option_search_button_func)
        self.entry_button.place(x=850, y=30)

        # create item icon
        self.items = []

    def option_search_button_func(self):
        name = str(self.entry.get())
        if not name:
            return

        self._make_item(name)

    def _make_item_icon(self, x, y):
        with urllib.request.urlopen(self.items[-1]["Info"][0]) as u:
             raw_data=u.read()
        im=Image.open(BytesIO(raw_data))
        self.image.append(ImageTk.PhotoImage(im))
        self.items[-1]["Icon"] = Button(self.window, image=self.image[-1])
        self.items[-1]["Icon"].place(x=x, y=y)
        

    def _make_item_name(self, x, y):
        self.items[-1]["Name"] = Label(self.window,  text=self.items[-1]["Info"][2],\
                                        font=self.font_search_item_name)
        self.items[-1]["Name"].place(x=x + 80, y=y + 20)

    def _delete_item(self):
        for item in self.items:
            for key, obj in item.items():
                if hasattr(obj, 'destroy'):
                    obj.destroy()
        self.items = []

    def _make_item(self, name):
        self.image = []

        # item delete
        self._delete_item()

        # API init
        new_API = APIprocess.Get_char_json(name)
        new_API.getAmorizes()

        def _make_item_each(func, x, y):
            self.items.append({})
            self.items[-1]["Info"] = func()
            self._make_item_icon(x, y)
            self._make_item_name(x, y)


        _make_item_each(new_API.GetplayerWeaponinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y)
        _make_item_each(new_API.GetplayerHeadinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 1 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerTopinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 2 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerUnderinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 3 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerHandsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 4 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerPauldronsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 5 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerBraceletinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 6 * SEARCH_ITEM_DIFF)
        
        _make_item_each(new_API.GetplayerNecklessinfo,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y)
        _make_item_each(new_API.GetplayerEarRing1info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 1 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerEarRing2info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 2 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerRing1info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 3 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerRing2info,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 4 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerStoneinfo,\
                       SEARCH_ITEM2_X, SEARCH_ITEM_Y + 5 * SEARCH_ITEM_DIFF)

    def option_goal_func(self):
        self.clear_objects()

    def option_todo_func(self):
        self.clear_objects()

    def option_history_func(self):
        self.clear_objects()

    def option_popup_func(self):
        self.clear_objects()


        
