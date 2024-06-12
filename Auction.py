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
            "Name": "string"
        }

        tansformed_data = json.dumps(data)
        self.response = requests.post(url, headers=self.postheaders, data=data)
        self.res = requests.get(url,headers=self.getheaders)
        self.jsonObject = self.res

b = getActionAPI()
b.getAction("")