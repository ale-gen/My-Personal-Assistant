import requests
from datetime import datetime
import sys


class WeatherManager:

    def __init__(self, personal_assistant, weather_data):
        self.personal_assistant = personal_assistant
        self.weather_data = weather_data

    def fetch_weather_json(self, api_key, city_name):
        base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric"
        url = base_url + f"&q={city_name}"
        try:
            response = requests.get(url)
            print(response.status_code)
            if response.status_code != 200:
                response = 'N/A'
                return -1
            else:
                data = response.json()
                print(data)
                data_encoder = self.weather_data(data)
                weather_data_encoded = data_encoder.decode_data()
                return weather_data_encoded
        except requests.exceptions.RequestException as error:
            print(error)
            sys.exit(1)

    def check_weather(self, api_key, city=None):
        if city is None:
            self.personal_assistant.respond("For which city do you want to check weather?")
            city = self.personal_assistant.talk()
        data = self.fetch_weather_json(api_key, city)
        if data != -1:
            answer = "In %s is currently %s and %s Celsius degree" % (
            data['city'], data['description'], data['temperature'])
            self.personal_assistant.respond(answer)
            self.personal_assistant.respond("Do you need more data?")
            user_answer = self.personal_assistant.talk()
            if user_answer == "yes":
                sunrise = data['sunrise']
                sunrise_hour = datetime.utcfromtimestamp(sunrise).strftime('%H:%M:%S')
                sunset = data['sunset']
                sunset_hour = datetime.utcfromtimestamp(sunset).strftime('%H:%M:%S')
                answer = "Minimum temperature today reaches %s Celsius degree, but maximum will be equal %s. Sunrise is \
                            at %s, sunset at %s" \
                         % (data['minimum temperature'], data['maximum temperature'], sunrise_hour, sunset_hour)
                self.personal_assistant.respond(answer)
                self.personal_assistant.respond("Do you want to know something more?")
                user_answer = self.personal_assistant.talk()
                if user_answer == "yes":
                    self.personal_assistant.respond("What do you want to?")
                    prompt = self.personal_assistant.talk()
                    try:
                        value = data[prompt]
                        answer = "The %s is equal %s" % (prompt, value)
                        self.personal_assistant.respond(answer)
                    except:
                        self.personal_assistant.respond("I can't get that data, I'm sorry")
                        self.personal_assistant.respond("Do you want to try again?")
        else:
            self.personal_assistant.respond("Sorry, I can't found out about weather it this city. Are you sure you gave me a correct data? Do you \
                    want to try again? ")
            user_answer = self.personal_assistant.talk()
            if user_answer == "yes":
                self.check_weather(api_key)