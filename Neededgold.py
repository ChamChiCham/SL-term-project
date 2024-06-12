import pandas as pd
from openpyxl import load_workbook
# pandas와 openpyxl 받아야함

weapon_Mul = 1.68
# 테스트를 위한 임시 리스트
testlist = ["", "", "", 19, "유물"]

class Neededgold:
    equipment = []
    upgrade_reinforce = 0
    undertag1420list = {}
    tag1420list = {}
    tag1520list = {}
    target_reinforce = 0
    equipment = []
    def __init__(self, equipment, target_reinforce):
        #1490 1520 1580
        # 목표 강화수치
        self.target_reinforce = target_reinforce
        # 현재 장비
        self.equipment = equipment
        ldwb = load_workbook("resorce.xlsx", data_only= True)
        ldwb = ldwb['Sheet1']
        get_cells = ldwb['B3':'B27']
        i = 1
        for row in get_cells:
            for cell in row:
                self.tag1420list[i] = cell.value
                i+=1

        get_cells2 = ldwb['D3':'D27']
        i = 1
        for row in get_cells2:
            for cell in row:
                self.tag1520list[i] = cell.value
                i+=1

        self.undertag1420list[19] = 4005
        self.undertag1420list[20] = 6116
        self.undertag1420list[21] = 6291
        self.undertag1420list[22] = 17918
        self.undertag1420list[23] = 18389
        self.undertag1420list[24] = 36529
        self.undertag1420list[25] = 38355

    def Output(self):
        sum = 0
        if self.equipment[4] == "유물":
            for i in self.undertag1420list.keys():
                if i == int(self.equipment[3]):
                    for j in range(i,int(self.target_reinforce)+1):
                        sum += self.undertag1420list[j]
        elif self.equipment[4] == "고대":
            if self.equipment[2].find("지배의 굴레") or self.equipment[2].find("배신의 구속") \
                    or self.equipment[2].find("갈망의 그을림") or self.equipment[2].find("파괴의 제물")\
                or self.equipment[2].find("매혹의 저주") or self.equipment[2].find("사멸의 종언") \
                    or self.equipment[2].find("악몽의 궤적") or self.equipment[2].find("환각의 가르침") \
                    or self.equipment[2].find("구원의 타륜") or self.equipment[2].find("광기의 지배") or self.equipment[2].find("욕망의 배신") \
                    or self.equipment[2].find("광기의 갈망") or self.equipment[2].find("마수의 파괴")\
                or self.equipment[2].find("욕망의 매혹") or self.equipment[2].find("마수의 사멸") \
                    or self.equipment[2].find("몽환의 악몽") or self.equipment[2].find("몽환의 환각") \
                    or self.equipment[2].find("군단의 구원"):
                for i in self.tag1520list.keys():
                    if i == int(self.equipment[3]):
                        for j in range(i, int(self.target_reinforce) + 1):
                            sum += self.tag1520list[j]
            else:
                for i in self.tag1420list.keys():
                    if i == int(self.equipment[3]):
                        for j in range(i, int(self.target_reinforce) + 1):
                            sum += self.tag1420list[j]
        else:
            sum = 0

        if self.equipment[1]=='무기':
            sum = sum * weapon_Mul

        return sum

# 테스트 잘 나옴
#k = Neededgold(testlist,24)
#b = k.Output()
#print(b)