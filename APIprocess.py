#Json 파일 피싱
import json
import webbrowser
import urllib.request
import urllib.parse

import os
import http.client

#open에 파일 이름삽입
import requests
from lostark_api_token import Token
import re


class Get_char_json:

    char_name = ""
    response = ""
    headers = {}
    jsonObject = ""
    returnList = []

    #닉네임으로 초기화 작업 실행
    def __init__(self, char_name):
        self.headers = {
            'accept': 'application/json',
            'authorization': Token
        }
        self.char_name = char_name

    def getAmorizes(self):
        url = 'https://developer-lostark.game.onstove.com/armories/characters/' + self.char_name + "/equipment"

        self.response = requests.get(url, headers=self.headers)
        self.jsonObject = self.response.json()
        print(self.jsonObject[1])
        #만약 전체 다 받아오고 싶으면
        # self.jsonObject[번호] << 이걸로 받아 오면 됨
        # 0 - 무기
        # 1 - 투구
        # 2 - 상의
        # 3 - 하의
        # 4 - 장갑
        # 5 - 어깨
        # 6 - 목걸이
        # 7 - 귀걸이
        # 8 - 귀걸이2
        # 9 - 반지
        # 10 - 반지2
        # 11 - 어빌리티스톤
        # 12 - 팔찌

# ---------------------- 장비 ----------------------------------------

    def GetplayerWeaponinfo(self):

        weaponinfo = []

        weaponinfo.append(self.jsonObject[0]["Icon"])
        weaponinfo.append(self.jsonObject[0]["Type"])
        weaponinfo.append(self.jsonObject[0]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[0]["Name"])
        if not(reinforce.isdigit()):
            weaponinfo.append('0')
        else:
            weaponinfo.append(reinforce)

        weaponinfo.append(self.jsonObject[0]["Grade"])
        index = self.jsonObject[0]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[0]["Tooltip"][index:index+20])
        weaponinfo.append(quality)

        return weaponinfo

    def GetplayerHeadinfo(self):

        Headinfo = []

        Headinfo.append(self.jsonObject[1]["Icon"])
        Headinfo.append(self.jsonObject[1]["Type"])
        Headinfo.append(self.jsonObject[1]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[1]["Name"])
        if not (reinforce.isdigit()):
            Headinfo.append('0')
        else:
            Headinfo.append(reinforce)

        Headinfo.append(self.jsonObject[1]["Grade"])
        index = self.jsonObject[1]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[1]["Tooltip"][index:index + 20])
        Headinfo.append(quality)

        return Headinfo

    def GetplayerTopinfo(self):

        Topinfo = []

        Topinfo.append(self.jsonObject[2]["Icon"])
        Topinfo.append(self.jsonObject[2]["Type"])
        Topinfo.append(self.jsonObject[2]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[2]["Name"])
        if not(reinforce.isdigit()):
            Topinfo.append('0')
        else:
            Topinfo.append(reinforce)

        Topinfo.append(self.jsonObject[2]["Grade"])
        index = self.jsonObject[2]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[2]["Tooltip"][index:index+20])
        Topinfo.append(quality)

        return Topinfo

    def GetplayerUnderinfo(self):

        underinfo = []

        underinfo.append(self.jsonObject[3]["Icon"])
        underinfo.append(self.jsonObject[3]["Type"])
        underinfo.append(self.jsonObject[3]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[3]["Name"])
        if not(reinforce.isdigit()):
            underinfo.append('0')
        else:
            underinfo.append(reinforce)

        underinfo.append(self.jsonObject[3]["Grade"])
        index = self.jsonObject[3]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[3]["Tooltip"][index:index+20])
        underinfo.append(quality)

        return underinfo

    def GetplayerHandsinfo(self):

        handsinfo = []

        handsinfo.append(self.jsonObject[4]["Icon"])
        handsinfo.append(self.jsonObject[4]["Type"])
        handsinfo.append(self.jsonObject[4]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[4]["Name"])
        if not(reinforce.isdigit()):
            handsinfo.append('0')
        else:
            handsinfo.append(reinforce)

        handsinfo.append(self.jsonObject[4]["Grade"])
        index = self.jsonObject[4]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[4]["Tooltip"][index:index+20])
        handsinfo.append(quality)

        return handsinfo

    def GetplayerPauldronsinfo(self):

        Pauldronsinfo = []

        Pauldronsinfo.append(self.jsonObject[5]["Icon"])
        Pauldronsinfo.append(self.jsonObject[5]["Type"])
        Pauldronsinfo.append(self.jsonObject[5]["Name"])
        reinforce = re.sub(r'[^0-9]', '', self.jsonObject[5]["Name"])
        if not(reinforce.isdigit()):
            Pauldronsinfo.append('0')
        else:
            Pauldronsinfo.append(reinforce)

        Pauldronsinfo.append(self.jsonObject[5]["Grade"])
        index = self.jsonObject[5]["Tooltip"].find("qualityValue")
        quality = re.sub(r'[^0-9]', '', self.jsonObject[5]["Tooltip"][index:index+20])
        Pauldronsinfo.append(quality)

        return Pauldronsinfo

#---------------------- 장신구 ----------------------------------------
    def GetplayerNecklessinfo(self):

        Necklessinfo = []

        Necklessinfo.append(self.jsonObject[6]["Icon"])
        Necklessinfo.append(self.jsonObject[6]["Type"])
        Necklessinfo.append(self.jsonObject[6]["Name"])

        Necklessinfo.append(self.jsonObject[6]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[6]["Tooltip"])

        property = tooltipsdict["Element_005"]['value']['Element_001']
        property = re.sub(r'<[^>]*>', '', property)
        Necklessinfo.append(property)


        #로드로 dict변환


        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        Necklessinfo.append(gackin1)
        Necklessinfo.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return Necklessinfo

    def GetplayerEarRing1info(self):

        EarRing1info = []

        EarRing1info.append(self.jsonObject[7]["Icon"])
        EarRing1info.append(self.jsonObject[7]["Type"])
        EarRing1info.append(self.jsonObject[7]["Name"])

        EarRing1info.append(self.jsonObject[7]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[7]["Tooltip"])

        property = tooltipsdict["Element_005"]['value']['Element_001']
        property = re.sub(r'<[^>]*>', '', property)
        EarRing1info.append(property)


        #로드로 dict변환


        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        EarRing1info.append(gackin1)
        EarRing1info.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return EarRing1info

    def GetplayerEarRing2info(self):

        EarRing2info = []

        EarRing2info.append(self.jsonObject[8]["Icon"])
        EarRing2info.append(self.jsonObject[8]["Type"])
        EarRing2info.append(self.jsonObject[8]["Name"])

        EarRing2info.append(self.jsonObject[8]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[8]["Tooltip"])

        property = tooltipsdict["Element_005"]['value']['Element_001']
        property = re.sub(r'<[^>]*>', '', property)
        EarRing2info.append(property)


        #로드로 dict변환


        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        EarRing2info.append(gackin1)
        EarRing2info.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return EarRing2info

    def GetplayerRing1info(self):

        Ring1info = []

        Ring1info.append(self.jsonObject[9]["Icon"])
        Ring1info.append(self.jsonObject[9]["Type"])
        Ring1info.append(self.jsonObject[9]["Name"])

        Ring1info.append(self.jsonObject[9]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[9]["Tooltip"])

        property = tooltipsdict["Element_005"]['value']['Element_001']
        property = re.sub(r'<[^>]*>', '', property)
        Ring1info.append(property)


        #로드로 dict변환


        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        Ring1info.append(gackin1)
        Ring1info.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return Ring1info

    def GetplayerRing2info(self):
        tagnum = 10
        Ring2info = []

        Ring2info.append(self.jsonObject[tagnum]["Icon"])
        Ring2info.append(self.jsonObject[tagnum]["Type"])
        Ring2info.append(self.jsonObject[tagnum]["Name"])

        Ring2info.append(self.jsonObject[tagnum]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[tagnum]["Tooltip"])

        property = tooltipsdict["Element_005"]['value']['Element_001']
        property = re.sub(r'<[^>]*>', '', property)
        Ring2info.append(property)

        # 로드로 dict변환

        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        Ring2info.append(gackin1)
        Ring2info.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return Ring2info

    def GetplayerStoneinfo(self):
        tagnum = 11
        Stoneinfo = []

        Stoneinfo.append(self.jsonObject[tagnum]["Icon"])
        Stoneinfo.append(self.jsonObject[tagnum]["Type"])
        Stoneinfo.append(self.jsonObject[tagnum]["Name"])

        Stoneinfo.append(self.jsonObject[tagnum]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[tagnum]["Tooltip"])

        # 로드로 dict변환

        gackin1 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_000']['contentStr']
        gackin1 = re.sub(r'<[^>]*>', '', gackin1)

        gackin2 = tooltipsdict["Element_006"]['value']['Element_000']['contentStr']['Element_001']['contentStr']
        gackin2 = re.sub(r'<[^>]*>', '', gackin2)

        Stoneinfo.append(gackin1)
        Stoneinfo.append(gackin2)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return Stoneinfo

    def GetplayerBraceletinfo(self):
        tagnum = 12
        Braceletinfo = []

        Braceletinfo.append(self.jsonObject[tagnum]["Icon"])
        Braceletinfo.append(self.jsonObject[tagnum]["Type"])
        Braceletinfo.append(self.jsonObject[tagnum]["Name"])

        Braceletinfo.append(self.jsonObject[tagnum]["Grade"])

        tooltipsdict = json.loads(self.jsonObject[tagnum]["Tooltip"])

        # 로드로 dict변환

        Braceeffect = tooltipsdict["Element_004"]['value']['Element_001']
        Braceeffect = re.sub(r'<[^>]*>', '', Braceeffect)

        Braceletinfo.append(Braceeffect)

        # Element_006여기부터 Element_000에 각인하나 001에 각인 하나 있음 이거 찾아야함

        return Braceletinfo

a = input()
b = Get_char_json(a)
b.getAmorizes()
c = b.GetplayerHeadinfo()
print(c)