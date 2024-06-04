from googlemaps import Client
import requests
import xml.etree.ElementTree as ET

########################################################
#   Googlemap에 getLocationData로 데이터 받아올 수 있음
#   fastfood[인덱스 번호]["name"] <- 이름
#   fastfood[인덱스 번호]["address"] <- 주소
#   fastfood[인덱스 번호]["lat"] <- 위도
#   fastfood[인덱스 번호]["lng"] <- 경도
########################################################

class Googlemap:
    fastfoods = []

    def __init__(self):
        api_key = "3b478912fd61494d95b72f2a6710c706"
        url = "https://openapi.gg.go.kr/Genrestrtfastfood?"

        params = {
            "Key": api_key,
            "Type" : "xml",
            "pindex": 3,
            "pSize" : 1000
        }

        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall("row")
        for item in items:
            if item.findtext("BIZPLC_NM").find("프랭크") != -1:
                fastfood = {
                    "name": item.findtext("BIZPLC_NM"),
                    "address": item.findtext("REFINE_ROADNM_ADDR"),
                    "lat": item.findtext("REFINE_WGS84_LAT"),
                    "lng": item.findtext("REFINE_WGS84_LOGT")
                }
                self.fastfoods.append(fastfood)

    def getLocationData(self):
        return self.fastfoods