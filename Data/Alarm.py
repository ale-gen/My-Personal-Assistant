from playsound import playsound
from datetime import datetime
import time


class Alarm:
    def __init__(self, personal_assistant):
        self.__personal_assistant = personal_assistant

    def set_alarm(self):
        file = "../Main/Phone_Ringing.mp3"
        self.__personal_assistant.respond("What hour this alarm is to be set?")
        alarm_hour = self.__personal_assistant.talk()
        if alarm_hour.isdigit() and 0 <= int(alarm_hour) < 24:
            alarm_hour = int(alarm_hour)
        else:
            self.__personal_assistant.respond("Incorrect hour, sorry")
            return
        self.__personal_assistant.respond(f"How many minutes after hour {alarm_hour}")
        alarm_minutes = self.__personal_assistant.talk()
        if alarm_minutes.isdigit() and 0 <= int(alarm_minutes) < 60:
            alarm_minutes = int(alarm_minutes)
        else:
            self.__personal_assistant.respond("Incorrect minutes, sorry")
            return

        while datetime.now().hour <= alarm_hour and datetime.now().minute < alarm_minutes:
            time.sleep(1)

        playsound(file, True)
