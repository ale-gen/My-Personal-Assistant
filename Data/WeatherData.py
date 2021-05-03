class WeatherData:
    def __init__(self, json_data):
        self.json_data = json_data

    def decode_data(self):
        code = self.json_data['cod']
        name = self.json_data['name']
        description = self.json_data['weather'][0]['description']
        temp = self.json_data['main']['temp']
        feels_like_temp = self.json_data['main']['feels_like']
        temp_min = self.json_data['main']['temp_min']
        temp_max = self.json_data['main']['temp_max']
        pressure = self.json_data['main']['pressure']
        humidity = self.json_data['main']['humidity']
        wind_speed = self.json_data['wind']['speed']
        sunrise = self.json_data['sys']['sunrise']
        sunset = self.json_data['sys']['sunset']
        weather_data = {"city": name, "description": description, "temperature": temp, "perceived temperature": feels_like_temp,
                        "minimum temperature": temp_min, "maximum temperature": temp_max, "pressure": pressure, "humidity": humidity,
                        "wind speed": wind_speed, "sunrise": sunrise, "sunset": sunset, "code": code}
        return weather_data
