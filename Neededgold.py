import pandas as pd
# pandas와 openpyxl 받아야함

class Neededgold:
    equipment = []
    upgrade_reinforce = 0
    def __init__(self, equipment, target_reinforce):
        #1490 1520 1580
        data = pd.read_excel("resorce.xlsx", engine= "openpyxl")
        print(data)

#        ...
#        if equipment[4] == '유물':
#            if int(equipment[3]) > target_reinforce :
#                return -1
#            else:
#                upgrade_reinforce = target_reinforce - int(equipment[3])

a = []
Neededgold(a,2)
