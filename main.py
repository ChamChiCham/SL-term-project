import APIprocess
import Neededgold

#name = input()

#new_API = APIprocess.Get_char_json(name)

# #꼭 먼저 선언
#new_API.getAmorizes()

# #리스트 형식으로 리턴받아야함, 필요한 것만 뽑아서 재가공함
# # 테스트--------------------------------------------------------------
#playerWeaponlist = new_API.GetplayerWeaponinfo()
# playerHeadlist = new_API.GetplayerHeadinfo()
# playerToplist = new_API.GetplayerTopinfo()
# playerUnderlist = new_API.GetplayerUnderinfo()
# playerHandlist = new_API.GetplayerHandsinfo()
# playershoulderlist = new_API.GetplayerPauldronsinfo()



playerNeckless = new_API.GetplayerNecklessinfo()
playerEarRing1 = new_API.GetplayerEarRing1info()
playerEarRing2 = new_API.GetplayerEarRing2info()
playerRing1 = new_API.GetplayerRing1info()
playerRing2 = new_API.GetplayerRing2info()
playerStone = new_API.GetplayerStoneinfo()
playerbracelet = new_API.GetplayerBraceletinfo()

#
# 무기/방어구   0.이미지 1.타입 2.이름 3.강화 4.등급 5.품질
# 장신구 0.이미지, 1. 타입 2. 이름 3. 등급 4. 특성 5. 각인1, 6. 각인2

# print("장비-------------")
#print(playerWeaponlist)
# print(playerHeadlist)
# print(playerToplist)
# print(playerUnderlist)
# print(playerHandlist)
# print(playershoulderlist)

print("장신구-------------")
print(playerNeckless)
print(playerEarRing1)
print(playerEarRing2)
print(playerRing1)
print(playerRing2)
print(playerStone)
print(playerbracelet)

#--------------------------------- Neededgold사용법 ---------------------------------------------
#print("목표 강화")
#r = input()
# ------ 인자로 APIprocess의 장비 리스트를 받고 목표 강화 수치를 받음 --------
#test = Neededgold.Neededgold(playerWeaponlist(Api프로세스의 장비 리스트),r(목표강화수치))

#필요 골드를 int/float으로 리턴함
#k = test.Output()
#print(k)

#   GUI설계 방향
#   1. 먼저 강화할 장비를 클릭
#   2. 강화할 장비의 목표 강화수치 입력
#   3. 골드 리턴
#--------------------------------- --------------- ---------------------------------------------

#from MainGUI import mainGUI

#mainGUI()
