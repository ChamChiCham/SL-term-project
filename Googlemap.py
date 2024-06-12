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
    map_url = ""
    response = ""
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
        zoom = 13

        Google_API_Key = 'AIzaSyCzFgc9OGnXckq1-JNhSCVGo9zIq1kSWcE'
        center_lat = ("37.5479258")
        center_lng = ("127.0569359")
        self.map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lng}&zoom={zoom}&size=400x400&maptype=roadmap"

        marker_urls = ""
        for fastfood in self.fastfoods:
            if fastfood['lat'] and fastfood['lng']:
                lat, lng = float(fastfood['lat']), float(fastfood['lng'])
                marker_urls += f"&markers=color:red%7C{lat},{lng}"

        self.map_url += marker_urls
        self.map_url += '&key=' + Google_API_Key
        print(self.map_url)

        self.response = requests.get(self.map_url)

    def getLocationData(self):
        return self.fastfoods

    def getMapUrl(self):
        return self.map_url

    def getResponse(self):
        return self.response

    def getName(self):
        self.namelist = []

        for i in self.fastfoods:
            self.namelist.append("name")


        return "성수역 모코코테마 프랭크버거 매장"

    def getAddress(self):
        return "서울 성동구 아차산로7나길 14"