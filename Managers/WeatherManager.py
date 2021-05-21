import requests
import sys
from Data.Weather import Weather


def fetch_weather_json(api_key, city_name):
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
            weather_data_encoded = decode_data(data)
            return weather_data_encoded
    except requests.exceptions.RequestException as error:
        print(error)
        sys.exit(1)


def check_weather(assistant, api_key, city=None):
    if city is None:
        assistant.respond("For which city do you want to check weather?")
        city = assistant.talk()
    data = fetch_weather_json(api_key, city)
    if data != -1:
        weather = Weather(data['city'], data['description'], data['temperature'], data['perceived temperature'],
                          data['minimum temperature'], data['maximum temperature'], data['pressure'], data['humidity'],
                          data['wind speed'], data['sunrise'], data['sunset'], data['code'])
        assistant.respond(weather.__str__())
        assistant.respond("Do you need more data?")
        user_answer = assistant.talk()
        if user_answer == "yes":
            assistant.respond(weather.detailed_description)
            assistant.respond("Do you want to know something more?")
            user_answer = assistant.talk()
            if user_answer == "yes":
                assistant.respond("What do you want to?")
                prompt = assistant.talk()
                try:
                    value = data[prompt]
                    answer = "The %s is equal %s" % (prompt, value)
                    assistant.respond(answer)
                except:
                    assistant.respond("I can't get that data, I'm sorry")
                    assistant.respond("Do you want to try again?")
    else:
        assistant.respond("Sorry, I can't found out about weather it this city. Are you sure you "
                          "gave me a correct data? Do you want to try again? ")
        user_answer = assistant.talk()
        if user_answer == "yes":
            check_weather(assistant, api_key)


def decode_data(json_data):
    code = json_data['cod']
    name = json_data['name']
    description = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    feels_like_temp = json_data['main']['feels_like']
    temp_min = json_data['main']['temp_min']
    temp_max = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = json_data['sys']['sunrise']
    sunset = json_data['sys']['sunset']
    weather_data = {"city": name, "description": description, "temperature": temp, "perceived temperature": feels_like_temp,
                    "minimum temperature": temp_min, "maximum temperature": temp_max, "pressure": pressure, "humidity": humidity,
                    "wind speed": wind_speed, "sunrise": sunrise, "sunset": sunset, "code": code}
    return weather_data