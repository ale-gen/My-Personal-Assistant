import sys
import time
import speech_recognition as sr
from gtts import gTTS # Google text to speech
from playsound import playsound # To play sound
import os # Save/open files
import datetime
from datetime import datetime
import random
import webbrowser
import json
import requests
import Data.WeatherData as wh
import TextFiles.FileData as fileData
import Data.Speech as sp
import Data.WeatherManager as wm
import Data.Alarm as am
from selenium import webdriver


def fetch_recipes_json(api_key, meal):
    base_url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}"
    url = base_url + f"&query={meal}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            response = 'N/A'
            return -1
        else:
            recipes_data = response.json()
            print(recipes_data)
            return None
    except requests.exceptions.RequestException as error:
        print(error)
        sys.exit(1)


if __name__=='__main__':
    personal_assistant = sp.Speech
    personal_assistant.respond("Hi, I am MPA.")
    help_commands = fileData.fetch_help_commands()
    bye_commands = fileData.fetch_bye_commands()
    api_keys = fileData.get_api_keys()

    while(1):
        help = random.randint(0, len(help_commands)-1)
        personal_assistant.respond(help_commands[help])
        order = personal_assistant.talk().lower()

        if 'bye' in str(order) or 'stop' in str(order) or 'exit' in str(order):
            bye = random.randint(0, len(bye_commands)-1)
            personal_assistant.respond(bye_commands[bye])
            break

        elif 'time' in order:
            actual_time = datetime.now().strftime("%H:%M:%S")
            personal_assistant.respond(f"It's {actual_time}")

        elif 'search' in order:
            order = order.replace("search", "")
            url = "https://www.google.com.tr/search?q={}".format(order)
            personal_assistant.respond(f"I am searching {order}")
            webbrowser.open_new_tab(url)
            time.sleep(5)

        elif 'open google' in order:
            webbrowser.open_new_tab("https://www.google.com/")
            personal_assistant.respond("Google is opening")
            time.sleep(5)

        elif 'location' in order:
            api_key = api_keys.get("GoogleMaps")
            webbrowser.open_new_tab(f"https://www.google.com/maps/@?api={api_key}&map_action=map&zoom=19")
            personal_assistant.respond("Maps are opening")
            time.sleep(5)

        elif 'alarm' in order:
            alarm = am.Alarm(personal_assistant)
            alarm.set_alarm()

        elif 'check weather' in order:
            api_key = api_keys.get("OpenWeather")
            weather_data = wh.WeatherData
            weather_manager = wm.WeatherManager(personal_assistant, weather_data)
            weather_manager.check_weather(api_key)

        elif 'open youtube' in order:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=xlt4JpaPzko")
            personal_assistant.respond("Youtube is opening")
            time.sleep(5)

        elif 'meal' in order:
            api_key = api_keys.get("Spoonacular")
            fetch_recipes_json(api_key, "pasta")