import schedule
import time


######################################################################
#
#       토글 형식으로 만들었음 time_job객체를 하나 생성하고 set을 통해
#       체크 상태 변경 가능 ( True 인지 False 인지 )
#       필요하면 get으로 가져올 수 있음
#       scheduleReset은 자동으로 일정 시간마다 실행되는 함수 << 이건 잘 되는지 모름
#
#######################################################################
class time_job:
    Guradian = False
    Chaos = False
    Epona = False
    def __init__(self):
        pass

    ##### 텔레그램 봇 알람 보내는 부분 ######
    def sendAlarm(self):
        pass

    ###### 알람 리셋 시키기 #############
    def resetAlarmdata(self):
        self.Guradian = False
        self.Chaos = False
        self.Epona = False

    def scheduleReset(self):
        schedule.every().day.at("00:00").do(self.send_alarm)
        schedule.every().day.at("00:00").do(self.reset_alarm_data())

    def setGuradian_toggle(self):
        if self.Guradian == True:
            self.Guradian = False
        else:
            self.Guradian = True

    def setChaos_toggle(self):
        if self.Chaos == True:
            self.Chaos = False
        else:
            self.Chaos = True

    def setEpona_toggle(self):
        if self.Epona == True:
            self.Epona = False
        else:
            self.Epona = True

    def getGuradian(self):
        return self.Guradian

    def getChaos(self):
        return self.Chaos

    def getEpona(self):
        return self.Epona