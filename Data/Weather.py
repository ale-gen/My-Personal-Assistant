from datetime import datetime


class Weather(object):
    def __init__(self, city, description, temp, perceived_temp, min_temp, max_temp, pressure, humidity, wind_speed,
                 sunrise, sunset, code):
        self.__city = city
        self.__descritpion = description
        self.__temperature = temp
        self.__perceived_temperature = perceived_temp
        self.__minimum_temperature = min_temp
        self.__maximum_temperature = max_temp
        self.__pressure = pressure
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__sunrise = sunrise
        self.__sunset = sunset
        self.__code = code

    @property
    def detailed_description(self):
        sunrise_hour = datetime.utcfromtimestamp(self.__sunrise).strftime('%H:%M:%S')
        sunset_hour = datetime.utcfromtimestamp(self.__sunset).strftime('%H:%M:%S')
        return "Minimum temperature today reaches %s Celsius degree, but maximum will be equal %s. Sunrise is \
                at %s, sunset at %s" % (self.__minimum_temperature, self.__maximum_temperature,
                                        sunrise_hour, sunset_hour)

    def __str__(self):
        return "In %s is currently %s and %s Celsius degree" % (self.__city, self.__descritpion, self.__temperature)