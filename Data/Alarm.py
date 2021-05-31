from playsound import playsound
from datetime import datetime
import time
import threading


class Alarm:
    def __init__(self, personal_assistant):
        self.__personal_assistant = personal_assistant
        self.__minutes = None
        self.__hours = None
        self.__time_to_wait = None

    def set_alarm(self):
        self.__personal_assistant.respond("What hour this alarm is to be set?")
        alarm_hour = self.__personal_assistant.talk()
        if alarm_hour.isdigit() and 0 <= int(alarm_hour) < 24:
            alarm_hour = int(alarm_hour)
            self.__hours = alarm_hour
        else:
            self.__personal_assistant.respond("Incorrect hour, sorry")
            return
        self.__personal_assistant.respond(f"How many minutes after hour {alarm_hour}")
        alarm_minutes = self.__personal_assistant.talk()
        if alarm_minutes.isdigit() and 0 <= int(alarm_minutes) < 60:
            alarm_minutes = int(alarm_minutes)
            self.__minutes = alarm_minutes
        else:
            self.__personal_assistant.respond("Incorrect minutes, sorry")
            return

        threading.Thread(target=self.wait_to_alarm).start()
        return 2

    def wait_to_alarm(self):
        file = "../Main/Phone_Ringing.mp3"
        count = 0
        while datetime.now().hour <= self.__hours and datetime.now().minute < self.__minutes:
            #print("I am waiting")
            count += 1
        playsound(file, True)

    def count_time_to_wait_sec(self):
        time_to_wait = 0
        if datetime.now().hour < self.__hours:
            time_to_wait = (60 - datetime.now().minute) * 60
            hours_to_wait = self.__hours - datetime.now().hour - 1
            time_to_wait += hours_to_wait * 60 * 60
            self.__time_to_wait = time_to_wait
            return time_to_wait
        elif datetime.now().hour == self.__hours:
            if datetime.now().minute < self.__minutes:
                time_to_wait = (self.__minutes - datetime.now().minute) * 60
                self.__time_to_wait = time_to_wait
                return time_to_wait
