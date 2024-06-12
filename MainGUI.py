import tkinter
from tkinter import *
from tkinter import font
from winsound import *
from functools import partial

import SearchDir
import alram
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
import Googlemap
import APIprocess
import Neededgold
from SearchDir import searchDir
import fileDuplicator
from PIL import Image, ImageTk
import io
import requests
#import spam
import re

OPTION_X = 50
OPTION_Y_DIFF = 120
OPTION1_Y = 80
OPTION2_Y = OPTION1_Y + OPTION_Y_DIFF
OPTION3_Y = OPTION2_Y + OPTION_Y_DIFF
OPTION4_Y = OPTION3_Y + OPTION_Y_DIFF
OPTION5_Y = OPTION4_Y + OPTION_Y_DIFF
OPTION6_Y = OPTION5_Y + OPTION_Y_DIFF
OPTION7_Y = OPTION6_Y + OPTION_Y_DIFF

OPTION_SIZE_X = 10
OPTION_SIZE_Y = 2

SEARCH_ENTRY_X = 300
SEARCH_ENTRY_Y = 100

SEARCH_ITEM1_X = 350
SEARCH_ITEM2_X = 800
SEARCH_ITEM_Y = 140
SEARCH_ITEM_DIFF = 120

GRAPH_WIDTH = 800
GRAPH_HEIGHT = 600

class mainGUI:
    def __init__(self):
        self.image = []
        self.window = Tk()
        self.window.title("너, 로아 열심히 하고 있니?")
        self.window.geometry("1280x960")
        self.window.configure(bg="black")
        self.im=Image.open(("background.png"))
        self.image.append(ImageTk.PhotoImage(self.im))
        self.label = Label(self.window, image = self.image[0])
        self.label.place(x=-2,y=-2)
        self.make_fonts()
        self.make_ui()
        self.objects = []
        self.option = "None"
        self.window.mainloop()
        self._search_image = []

    def make_fonts(self):
        self.font_option = font.Font(self.window, size=20, family='맑은 고딕', weight="bold")
        self.font_search_entry = self.font_option
        self.font_search_item_name = font.Font(self.window, size=14, family='맑은 고딕')
        self.font_history = font.Font(self.window, size=24, family='맑은 고딕', weight="bold")
        self.font_database = font.Font(self.window, size=30, family='맑은 고딕', weight="bold")

    def make_ui(self):

        self.option_search = Button(self.window, text="유저 검색",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_search_func, bg="white")
        self.option_search.place(x=OPTION_X,y=OPTION1_Y)

        self.option_goal = Button(self.window,text="목표치 설정", \
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_goal_func, bg="white")
        self.option_goal.place(x=OPTION_X,y=OPTION2_Y)

        self.option_todo = Button(self.window,text="내 할일",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_todo_func, bg="white")
        self.option_todo.place(x=OPTION_X,y=OPTION3_Y)

        self.option_history = Button(self.window,text="검색 기록", \
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_history_func, bg="white")
        self.option_history.place(x=OPTION_X,y=OPTION4_Y)

        self.option_popup = Button(self.window,text="팝업 스토어",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_popup_func, bg="white")
        self.option_popup.place(x=OPTION_X,y=OPTION5_Y)

        self.option_graph = Button(self.window,text="그래프",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_graph_func, bg="white")
        self.option_graph.place(x=OPTION_X,y=OPTION6_Y)

        self.option_database = Button(self.window,text="순위",\
                                    width=OPTION_SIZE_X, height=OPTION_SIZE_Y,\
                                    font=self.font_option, command=self.option_database_func, bg="white")
        self.option_database.place(x=OPTION_X,y=OPTION7_Y)

    def clear_objects(self):
        for object in self.objects:
            object.destroy()
        self.objects = []




        match self.option:
            case "Search":
                self.option_search.configure(bg="white")
                self._delete_items()
            case "Goal":
                self.option_goal.configure(bg="white")
                self._delete_items()
            case "Todo":
                self.option_todo.configure(bg="white")
                self.label.destroy()
            case "History":
                self.option_history.configure(bg="white")
            case "Popup":
                self.option_popup.configure(bg="white")
                self.map_image[0].destroy()
                self.label.destroy()
    
            case "Graph":
                self.option_graph.configure(bg="white")
                self._delete_items()
                for label in self.graph_labels:
                    label.destroy()
            case "Database":
                self.option_database.configure(bg="white")

    def option_search_func(self):
        # clear objects
        self.clear_objects()
        self.option = "Search"
        self.option_search.configure(bg="yellow")

        self._make_search_entry()

    def option_goal_func(self):
        # clear objects
        self.clear_objects()
        self.option = "Goal"
        self.option_goal.configure(bg="yellow")

        self.objects.append(Label(self.window, text="Goal: ", font=self.font_search_entry))
        self.goal_label = self.objects[-1]
        self.goal_label.place(x=800,y=875)

        self.goal_entry = None

        self._make_search_entry()

    def option_todo_func(self):
        self.clear_objects()
        self.option = "Todo"
        self.option_todo.configure(bg="yellow")

        self.imTodoback=Image.open(("roacon.jpg"))
        self.image.append(ImageTk.PhotoImage(self.imTodoback))
        self.label = Label(self.window, image = self.image[1])
        self.label.place(x=270,y=160)

        self.objects.append(Entry(self.window, font=self.font_search_entry))
        self.objects[0].bind("<Return>", self._do_id)
        self.entry = self.objects[0]
        self.objects.append(Entry(self.window, font=self.font_search_entry))
        self.objects[1].bind("<Return>", self._do_id)
        self.entry2 = self.objects[1]
        self.objects.append(Button(self.window, width=10, height=5, command=self._setChaos))
        self.objects.append(Button(self.window, width=10, height=5, command=self._setEpona))
        self.objects.append(Button(self.window, width=10, height=5, command=self._setGuardian))

        self.objects[0].place(x=700, y=50)
        self.objects[1].place(x=700, y=110)
        self.objects[2].place(x=400, y=400)
        self.objects[3].place(x=700, y=400)
        self.objects[4].place(x=1000, y=400)

        self.objects.append(Label(self.window, text="X", font=self.font_search_entry))
        self.objects.append(Label(self.window, text="X", font=self.font_search_entry))
        self.objects.append(Label(self.window, text="X", font=self.font_search_entry))
        self.objects[5].place(x=420, y=600)
        self.objects[6].place(x=720, y=600)
        self.objects[7].place(x=1020, y=600)

        self.objects.append(Label(self.window,text = "메일 입력", font = self.font_search_entry))
        self.objects.append(Label(self.window,text = "텔레그램 코드 입력", font = self.font_search_entry))
        self.objects.append(Label(self.window,text = "내 할일 설정하기", font = self.font_search_entry))
        self.objects.append(Label(self.window,text = "카오스 게이트", font = self.font_search_entry))
        self.objects.append(Label(self.window,text = "에포나 일일 퀘스트", font = self.font_search_entry))
        self.objects.append(Label(self.window,text = "가디언 토벌", font = self.font_search_entry))

        self.objects[8].place(x=400, y=50)
        self.objects[9].place(x=400, y=110)
        self.objects[10].place(x=630, y=200)
        self.objects[11].place(x=350, y=300)
        self.objects[12].place(x=620, y=300)
        self.objects[13].place(x=960, y=300)

    def _setChaos(self):
        self._tj.setChaos_toggle()
        text = ""
        if self._tj.getChaos() == False:
            text = "X"
        else:
            text = "O"

        self.objects[5].configure(text=text)
        self._tj.sendAlarm()

    def _setEpona(self):
        self._tj.setEpona_toggle()
        text = ""
        if self._tj.getEpona() == False:
            text = "X"
        else:
            text = "O"

        self.objects[6].configure(text=text)
        self._tj.sendAlarm()

    def _setGuardian(self):
        self._tj.setGuradian_toggle()
        text = ""
        if self._tj.getGuradian() == False:
            text = "X"
        else:
            text = "O"

        self.objects[7].configure(text=text)
        self._tj.sendAlarm()

    def option_history_func(self):
        self.clear_objects()
        self.option = "History"
        self.option_history.configure(bg="yellow")

        text = "검색기록\n\n"
        duplicator = []
        duplicator = fileDuplicator.fileDuplicator().getHistory()
        for s in duplicator:
            text += s
        text = text[:-1]

        self.objects.append(Label(self.window, text=text, font=self.font_history))
        self.objects[-1].place(x=600, y=150)

    def option_popup_func(self):
        self.map_image = []
        self.mokoko_image =[]
        self.clear_objects()
        self.option = "Popup"
        self.option_popup.configure(bg="yellow")

        gm = Googlemap.Googlemap()
        self.url = gm.getMapUrl()
        #self.url = "https://maps.googleapis.com/maps/api/staticmap?center=37.3719161438,127.1623145413&zoom=13&size=400x400&maptype=roadmap&markers=color:red%7C37.3719161438,127.1623145413&key=AIzaSyCzFgc9OGnXckq1-JNhSCVGo9zIq1kSWcE"
        self.response = requests.get(self.url)
        self.images = Image.open(BytesIO(self.response.content))
        self.immokoko=Image.open(("mokoko_background.png"))
        self.mokoko_image.append(ImageTk.PhotoImage(self.immokoko))
        self.label = Label(self.window, image = self.mokoko_image[0])
        self.label.place(x=400,y=100)
        self.tk_image = ImageTk.PhotoImage(self.images)
        # 지도 이미지 라벨 생성
        self.map_image.append(Label(self.window,image=self.tk_image))
        self.map_image[0].place(x=550,y=400)
        self.namelist = gm.getName()
        self.address = gm.getAddress()
        self.objects.append(Label(self.window,text = "모코코 팝업 프랭크 버거", font = self.font_history))
        self.objects.append(Label(self.window,text = self.namelist,font = self.font_option))
        self.objects.append(Label(self.window,text = "주소 : " + self.address,font = self.font_option))
        self.objects[0].place(x=570,y=120)
        self.objects[1].place(x=530,y=360)
        self.objects[2].place(x=510,y=800)

    def option_graph_func(self):
        self.clear_objects()
        self.option = "Graph"
        self.option_graph.configure(bg="yellow")

        self._make_search_entry()

        self.graph_labels = []
        
        self.objects.append(Canvas(self.window, width=GRAPH_WIDTH, height=GRAPH_HEIGHT, bg="white", bd=2))
        self.objects[-1].place(x=350, y=200)
        self.graph = self.objects[-1]
    
    def option_database_func(self):
        self.clear_objects()
        self.option = "Database"
        self.option_database.configure(bg="yellow")

        text = "\n"

        # DATABASE
        text = self._get_database()

        self.objects.append(Label(self.window, text=text, font=self.font_database))
        self.objects[-1].place(x=500, y=200)

    def _make_search_entry(self):
        self.objects.append(Entry(self.window, font=self.font_search_entry))
        self.objects[-1].bind("<Return>", self._do_search)
        self.objects[-1].place(x=500, y=50)
        self.entry = self.objects[-1]
        self.objects.append(Button(self.window, width=10, height=5, command=self._do_search))
        self.objects[-1].place(x=850, y=30)
        self.entry_button = self.objects[-1]

        self.items = []

    def _do_search(self, event=None):
        name = str(self.entry.get())
        SearchDir.searchDir(name)
        if not name:
            return
        if self.option == "Graph":
            self._make_graph(name)
        else:
            self._make_item(name)

    def _write_database(self, name, level):
        if not name or not level:
            return 
        
        level = level.replace(",", "")
        flevel = float(level)
        spam.write(name.encode('cp949'), flevel)

    def _get_database(self):
        text = "유저 순위\n\n"

        cp949_datas = spam.get()
        data = []
        for st in cp949_datas:
            data.append(st.decode('cp949'))
        
        cnt = 1
        for s in data:
            if s:
                new_API = APIprocess.Get_char_json(s)
                new_API.getAmorizes()
                level = new_API.GetplayerLevel()
                text += f"{cnt}위: {s} | {level}\n"
                cnt += 1
        text = text[:-1]
        return text

    def _make_graph(self, name):
        new_API = APIprocess.Get_char_json(name)
        new_API.getAmorizes()
        
        # DATABASE
        self._write_database(name, new_API.GetplayerLevel())


        self._delete_items()
        self._idx = 0

        def _make_item_each(func, x, y):
            self.items.append({})
            self.items[-1]["Info"] = func()
            self.items[-1]["x"] = x
            self.items[-1]["y"] = y
            self._make_item_icon()
            self._idx += 1

        self.graph.delete("all")

        func = []
        func.append(new_API.GetplayerHeadinfo)
        func.append(new_API.GetplayerTopinfo)
        func.append(new_API.GetplayerUnderinfo)
        func.append(new_API.GetplayerHandsinfo)
        func.append(new_API.GetplayerPauldronsinfo)
        func.append(new_API.GetplayerWeaponinfo)
        
        data = []
        for i in range(6):
            data.append(eval(func[i]()[3]))


        x_diff = GRAPH_WIDTH / len(data)
        y_diff = GRAPH_HEIGHT / 25
        x1 = 0
        x2 = x_diff
        y1 = GRAPH_HEIGHT


        for label in self.graph_labels:
            label.destroy()
        self.graph_labels = []

        for i in data:
            y2 = GRAPH_HEIGHT - y_diff * i
            self.graph.create_rectangle(x1 + 20, y1, x2 - 20, y2, fill="blue")
            x1 += x_diff
            x2 += x_diff
            _make_item_each(func[self._idx], x1 + 350 - 100, y1 + 220)
            self.graph_labels.append(Label(self.window, text=str(i), font=self.font_option, bg="white"))
            self.graph_labels[-1].place(x=x1 + 265, y= y2 + 150)
        
    def _make_item(self,name):

        self._search_image = []

        # item delete
        self._delete_items()
        self._idx = 0

        # API init
        new_API = APIprocess.Get_char_json(name)
        new_API.getAmorizes()

        # DATABASE
        self._write_database(name, new_API.GetplayerLevel())

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
        
        if self.option == "Goal":
            return

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
        self._search_image.append(ImageTk.PhotoImage(im))
        self.items[-1]["Icon"] = Button(self.window, image=self._search_image[-1])

        if self.option == "Search":
            self.items[-1]["Icon"].bind("<Button-1>", partial(self._item_exp_on, self._idx))
            self.items[-1]["Icon"].bind("<ButtonRelease-1>", partial(self._item_exp_off, self._idx))
        else:
            self.items[-1]["Icon"].bind("<ButtonRelease-1>", partial(self._item_set_goal, self._idx))

        self.items[-1]["Icon"].place(x=self.items[-1]["x"], y=self.items[-1]["y"])

    def _item_exp_on(self, idx, event):

        text = str()
        cnt = 0
        for i in range(1, len(self.items[idx]["Info"])):
            temp = self.items[idx]["Info"][i]
            for j in range(50, len(self.items[idx]["Info"][i]), 50):
                 temp = temp[:j] + '\n' + temp[j:]
                 cnt += 1
            text += temp
            if i != len(self.items[idx]["Info"]) - 1:
                text += '\n'

        self.items[idx]["Exp"] = Label(self.window, text=text, font=self.font_search_item_name)
        if idx == 6:
            self.items[idx]["Exp"].place(x=event.x + self.items[idx]["x"],\
                                         y=event.y + self.items[idx]["y"] - (100 + 25 * cnt))
        else:
            self.items[idx]["Exp"].place(x=event.x + self.items[idx]["x"],\
                                         y=event.y + self.items[idx]["y"])

    def _item_exp_off(self, idx, event):
        self.items[idx]["Exp"].destroy()

    def _item_set_goal(self, idx, event):

        if self.goal_entry != None:
            self.goal_entry.destroy()
            self.objects.pop()

        self.objects.append(Entry(self.window, font=self.font_search_entry, width=3))
        self.objects[-1].bind("<Return>", partial(self._item_show_goal, idx))
        self.objects[-1].place(x=event.x + self.items[idx]["x"] + 10,\
                               y=event.y + self.items[idx]["y"] + 10)
        self.goal_entry = self.objects[-1]

    def _item_show_goal(self, idx, event):
        goal_api = Neededgold.Neededgold(self.items[idx]["Info"], int(self.goal_entry.get()))
        self.goal_label.configure(text="Goal: "+ str(goal_api.Output()))
        self.goal_entry.destroy()
        self.goal_entry = None
        self.objects.pop()

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

    def _do_id(self, event=None):
        email = str(self.entry.get())
        name = str(self.entry2.get())
        if not name:
            return
        if not email:
            return

        self._sendmail(name,email)

    def _sendmail(self, name,email):
        self._tj = alram.time_job(user_id = name)
        print(name)
        self._tj.sendMail(email)
