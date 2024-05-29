import requests
from lostark_api_token import Token
import json

class getActionAPI:

    #품질 등등 생성자에 추가
    char_item_name = ""
    def __init__(self):
        self.postheaders = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'authorization': Token
        }

        self.getheaders = {
            'accept': 'application/json',
            'authorization': Token
        }


    def getAction(self, char_item_name):
        #url 변경
        char_item_name = ""
        url = 'https://developer-lostark.game.onstove.com/auctions/items'

        data = {
            "ItemLevelMin": 0,
            "ItemLevelMax": 0,
            "ItemGradeQuality": None,
            "SkillOptions": [
                {
                    "FirstOption": None,
                    "SecondOption": None,
                    "MinValue": None,
                    "MaxValue": None
                }
            ],
            "EtcOptions": [
                {
                    "FirstOption": None,
                    "SecondOption": None,
                    "MinValue": None,
                    "MaxValue": None
                }
            ],
            "Sort": "BIDSTART_PRICE",
            "CategoryCode": 0,
            "CharacterClass": None,
            "ItemTier": None,
            "ItemGrade": None,
            "ItemName": None,
            "PageNo": 0,
            "SortCondition": "ASC"
        }

        tansformed_data = json.dumps(data)
        self.response = requests.post(url, headers=self.postheaders, data=tansformed_data)

        self.res = requests.get(url,headers=self.getheaders)
        self.jsonObject = self.res
        print(self.response)
        print(self.jsonObject)

b = getActionAPI()
b.getAction("공허")