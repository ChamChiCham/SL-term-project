import APIprocess

class getActionAPI:

    #품질 등등 생성자에 추가
    char_item_name = ""
    def __init__(self, char_item_name):
        self.headers = {
            'accept': 'application/json',
            'authorization': Token
        }
        self.char_name = char_item_name

    def getAction(self):
       #url 변경

        url = 'https://developer-lostark.game.onstove.com/auctions/items/'

        data = {
            "ItemLevelMin": 0,
            "ItemLevelMax": 0,
            "ItemGradeQuality": null,
            "SkillOptions": [
                {
                    "FirstOption": null,
                    "SecondOption": null,
                    "MinValue": null,
                    "MaxValue": null
                }
            ],
            "EtcOptions": [
                {
                    "FirstOption": null,
                    "SecondOption": null,
                    "MinValue": null,
                    "MaxValue": null
                }
            ],
            "Sort": "BIDSTART_PRICE",
            "CategoryCode": 0,
            "CharacterClass": "string",
            "ItemTier": null,
            "ItemGrade": "string",
            "ItemName": self.char_name_item,
            "PageNo": 0,
            "SortCondition": "ASC"
        }


        self.response = requests.get(url,headers=self.headers, data = data)
        self.jsonObject = self.response.json()

