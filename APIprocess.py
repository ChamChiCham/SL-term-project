#Json 파일 피싱
import json
import webbrowser
import urllib.request
import urllib.parse

import os
import http.client

#open에 파일 이름삽입
import requests
import json
from lostark_api_token import Token

headers = {
    'accept': 'application/json',
    'authorization': Token
}

url = 'https://developer-lostark.game.onstove.com/news/events'

response = requests.get(url, headers=headers)
jsonObject = response.json()

print(response)
print(jsonObject)