import schedule
import time

class time_job:
    Guradian = False
    Chaos = False
    Epona = False
    def __init__(self):
        pass

    ##### 텔레그램 봇 알람 보내는 부분 ######
    def send_alarm(self):
        pass

    ###### 알람 리셋 시키기 #############
    def reset_alarm_data(self):
        pass

    def schedule(self):
        schedule.every().day.at("00:00").do(self.send_alarm)
        schedule.every().day.at("00:00").do(self.reset_alarm_data())