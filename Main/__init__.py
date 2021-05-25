import time
from datetime import datetime
import random
import webbrowser
import TextFiles.FileData as fileData
import Data.Speech as sp
import Data.Alarm as am
import Managers.WeatherManager as wm
import Managers.RecipeManager as rm
import Managers.LanguageManager as lm
import Managers.YoutubeManager as ym
import Managers.MapsManager as mm


if __name__ == '__main__':
    personal_assistant = sp.Speech
    personal_assistant.respond("Hi, I am MPA.")
    help_commands = fileData.fetch_help_commands()
    bye_commands = fileData.fetch_bye_commands()
    api_keys = fileData.get_api_keys()

    while 1:
        help = random.randint(0, len(help_commands)-1)
        personal_assistant.respond(help_commands[help])
        order = ""
        while order == "":
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

        elif 'location' in order:
            api_key = api_keys.get("GoogleMaps")
            webbrowser.open_new_tab(f"https://www.google.com/maps/@?api={api_key}&map_action=map&zoom=19")
            personal_assistant.respond("Maps are opening")

        elif 'alarm' in order:
            alarm = am.Alarm(personal_assistant)
            alarm.set_alarm()

        elif 'weather' in order:
            api_key = api_keys.get("OpenWeather").split("\n")[0]
            wm.check_weather(personal_assistant, api_key)

        elif 'open youtube' in order:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=xlt4JpaPzko")
            personal_assistant.respond("Youtube is opening")

        elif 'meal' in order:
            api_key = api_keys.get("Spoonacular").split("\n")[0]
            personal_assistant.respond("Give me the meal or tell random if you would like to draw for you.")
            answer = personal_assistant.talk()
            if 'random' in answer:
                rm.check_recipe(personal_assistant, api_key, True)
            else:
                rm.check_recipe(personal_assistant, api_key, False, answer)

        elif 'translate' in order:
            answer = True
            while answer:
                lm.service_sentence(personal_assistant)
                personal_assistant.respond("Do you want to translate something else? ")
                answer = personal_assistant.talk()
                if answer != "yes":
                    answer = False

        elif 'detect' in order:
            # Detect language with gui (TextField to copy the sentence to detect language
            pass

        elif 'youtube' in order:
            ym.manage_youtube(personal_assistant)

        elif 'maps' in order:
            mm.manage_maps(personal_assistant)
