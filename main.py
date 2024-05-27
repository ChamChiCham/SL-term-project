# import APIprocess

# name = input()

# new_API = APIprocess.Get_char_json(name)

# #꼭 먼저 선언
# new_API.getAmorizes()

# #리스트 형식으로 리턴받아야함, 필요한 것만 뽑아서 재가공함
# # 테스트--------------------------------------------------------------
# playerWeaponlist = new_API.GetplayerWeaponinfo()
# playerHeadlist = new_API.GetplayerHeadinfo()
# playerToplist = new_API.GetplayerTopinfo()
# playerUnderlist = new_API.GetplayerUnderinfo()
# playerHandlist = new_API.GetplayerHandsinfo()
# playershoulderlist = new_API.GetplayerPauldronsinfo()



# playerNeckless = new_API.GetplayerNecklessinfo()
# playerEarRing1 = new_API.GetplayerEarRing1info()
# playerEarRing2 = new_API.GetplayerEarRing2info()
# playerRing1 = new_API.GetplayerRing1info()
# playerRing2 = new_API.GetplayerRing2info()
# playerStone = new_API.GetplayerStoneinfo()
# playerbracelet = new_API.GetplayerBraceletinfo()

# #리스트 삽입 순서는 1.이미지 2.타입 3.이름 4.강화 5.등급 6.품질

# print("장비-------------")
# print(playerWeaponlist)
# print(playerHeadlist)
# print(playerToplist)
# print(playerUnderlist)
# print(playerHandlist)
# print(playershoulderlist)

# print("장신구-------------")
# print(playerNeckless)
# print(playerEarRing1)
# print(playerEarRing2)
# print(playerRing1)
# print(playerRing2)
# print(playerStone)
# print(playerbracelet)

from MainGUI import mainGUI

mainGUI()