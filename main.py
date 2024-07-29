import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from config import weather_token

def get_weather(city, weather_token):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(str(result))
        api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon="+str(location.longitude) + "&units=metric&exclude=hourly&appid=e16dc2de203cbc405ab50454004471cc"
        json_data = requests.get(api).json()

        # current temp
        temp = json_data['current']['temp']
        day1 = json_data['daily'][0]['weather'][0]['main']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']

        # day2 cell
        temp_day2 = json_data['daily'][2]['temp']['day']
        wind_day2 = json_data['daily'][2]['wind_speed']
        pressure_day2 = json_data['daily'][2]['pressure']
        day2 = json_data['daily'][1]['weather'][0]['main']
        # day3 cell
        temp_day3 = json_data['daily'][2]['temp']['day']
        wind_day3 = json_data['daily'][2]['wind_speed']
        day3 = json_data['daily'][2]['weather'][0]['main']
        # day4 cell
        temp_day4 = json_data['daily'][3]['temp']['day']
        wind_day4 = json_data['daily'][3]['wind_speed']
        day4 = json_data['daily'][3]['weather'][0]['main']
        # day5 cell
        temp_day5 = json_data['daily'][4]['temp']['day']
        wind_day5 = json_data['daily'][4]['wind_speed']
        day5 = json_data['daily'][4]['weather'][0]['main']
        # day6 cell
        temp_day6 = json_data['daily'][5]['temp']['day']
        wind_day6 = json_data['daily'][5]['wind_speed']
        day6 = json_data['daily'][5]['weather'][0]['main']
        # day7 cell
        temp_day7 = json_data['daily'][6]['temp']['day']
        wind_day7 = json_data['daily'][6]['wind_speed']
        day7 = json_data['daily'][6]['weather'][0]['main']

        # temp_day3 = json_data['daily'][2]['weather']['main']
        temp_day5 = json_data['daily'][0]['temp']['day']
        print(str(temp) + "|" + str(day1), str(temp_day2) + "|" +
              str(day2) + "|" + str(wind_day2) + "|" + str(pressure_day2))
        #print(json_data['daily'][6]['weather'][0]['main'])
        #print(str(temp) + "\n" + str( humidity) + "\n" + str(pressure) + "\n" + str(wind) + "\n" + str(description) + "\n")
        #print("next: \n" + str(temp_day2) + "\n" + str(temp_day3) + "\n" + str(temp_day5))
    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город")

    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
