from tkinter import *
from tkinter import font
from winsound import *
from functools import partial

from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk

import APIprocess
import Neededgold

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

        self.make_fonts()        
        self.make_ui()
        
        self.objects = []
        self.option = "None"
        self.window.mainloop()

    def make_fonts(self):
        self.font_option = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_entry = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_item_name = font.Font(self.window, size=14, family='맑은 고딕')

    def make_ui(self):
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

    def clear_objects(self):
        for object in self.objects:
            object.destroy()
        self.objects = []

        match self.option:
            case "Search":
                self._delete_items()
            case "Goal":
                self._delete_items()   
            case _:
                pass

    def option_search_func(self):
        # clear objects
        self.clear_objects()
        self.option = "Search"

        self._make_search_entry()


    def option_goal_func(self):
        # clear objects
        self.clear_objects()
        self.option = "Goal"

        self.objects.append(Label(self.window, text="Goal: ", font=self.font_search_entry))
        self.goal = self.objects[-1]
        self.goal.place(x=800,y=875)

        self._make_search_entry()

    def option_todo_func(self):
        self.clear_objects()
        self.option = "Todo"

    def option_history_func(self):
        self.clear_objects()
        self.option = "History"

    def option_popup_func(self):
        self.clear_objects()
        self.option = "Popup"


    def _make_search_entry(self):
        self.objects.append(Entry(self.window, font=self.font_search_entry))
        self.objects[-1].bind("<Return>", self._search_start_func)
        self.objects[-1].place(x=500, y=50)
        self.entry = self.objects[-1]

        self.objects.append(Button(self.window, width=10, height=5, command=self._search_start_func))
        self.objects[-1].place(x=850, y=30)
        self.entry_button = self.objects[-1]

        self.items = []

    def _search_start_func(self, event=None):
        name = str(self.entry.get())
        if not name:
            return

        self._make_item(name)

    def _make_item(self,name):
        self.image = []

        # item delete
        self._delete_items()
        self._idx = 0

        # API init
        new_API = APIprocess.Get_char_json(name)
        new_API.getAmorizes()

        def _make_item_each(func, x, y):
            self.items.append({})
            self.items[-1]["Info"] = func()
            self.items[-1]["x"] = x
            self.items[-1]["y"] = y
            self._make_item_icon()
            self._make_item_name()
            self._idx += 1


        _make_item_each(new_API.GetplayerHeadinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y)
        _make_item_each(new_API.GetplayerTopinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 1 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerUnderinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 2 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerHandsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 3 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerPauldronsinfo,\
                       SEARCH_ITEM1_X, SEARCH_ITEM_Y + 4 * SEARCH_ITEM_DIFF)
        _make_item_each(new_API.GetplayerWeaponinfo,\
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

    def _make_item_icon(self):
        with urllib.request.urlopen(self.items[-1]["Info"][0]) as u:
             raw_data=u.read()
        im=Image.open(BytesIO(raw_data))
        self.image.append(ImageTk.PhotoImage(im))
        self.items[-1]["Icon"] = Button(self.window, image=self.image[-1])

        if self.option == "Search":
            self.items[-1]["Icon"].bind("<Button-1>", partial(self._item_exp_on, self._idx))
            self.items[-1]["Icon"].bind("<ButtonRelease-1>", partial(self._item_exp_off, self._idx))
        else:
            self.items[-1]["Icon"].configure(command=partial(self._item_set_goal, self._idx))

        self.items[-1]["Icon"].place(x=self.items[-1]["x"], y=self.items[-1]["y"])

    def _item_exp_on(self, idx, event):

        text = str()
        for i in range(1, len(self.items[idx]["Info"])):
            text += self.items[idx]["Info"][i]
            if i != len(self.items[idx]["Info"]) - 1:
                text += '\n'

        self.items[idx]["Exp"] = Label(self.window, text=text, font=self.font_search_item_name)
        if idx == 6:
            self.items[idx]["Exp"].place(x=event.x + self.items[idx]["x"],\
                                         y=event.y + self.items[idx]["y"] - 100)
        else:
            self.items[idx]["Exp"].place(x=event.x + self.items[idx]["x"],\
                                         y=event.y + self.items[idx]["y"])

    def _item_exp_off(self, idx, event):
        self.items[idx]["Exp"].destroy()

    def _item_set_goal(self, idx):
        goal_api = Neededgold.Neededgold(self.items[idx]["Info"], 24)
        print(goal_api.Output())

    def _make_item_name(self):
        self.items[-1]["Name"] = Label(self.window,  text=self.items[-1]["Info"][2],\
                                        font=self.font_search_item_name)
        self.items[-1]["Name"].place(x=self.items[-1]["x"] + 80, y=self.items[-1]["y"] + 20)

    def _delete_items(self):
        for item in self.items:
            for key, obj in item.items():
                if hasattr(obj, 'destroy'):
                    obj.destroy()
        self.items = []
