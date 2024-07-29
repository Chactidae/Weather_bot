import requests
from aiogram.dispatcher import Dispatcher
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
from config import weather_token
import config
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.utils import executor
from translate import Translator

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("kon ni chi ha! Введи город, в котором ты хочешь узнать погоду!")

@dp.message_handler(lambda message: 'weather' in message.text.lower(), content_types=['text'])
async def get_weather(message: types.Message):

        comm = message.text.split(' ')
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(comm[1])

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(str(result))
        api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon="+str(location.longitude) + "&units=metric&exclude=hourly&appid=e16dc2de203cbc405ab50454004471cc"
        json_data = requests.get(api).json()
        if len(comm) == 2:
                temp_day2 = json_data['daily'][1]['temp']['day']
                wind_day2 = json_data['daily'][1]['wind_speed']
                pressure_day2 = json_data['daily'][1]['pressure']
                humidity2 = json_data['daily'][1]['humidity']
                day2 = json_data['daily'][1]['weather'][0]['main']

                forecast = ""
                dayWeek = datetime.now().strftime("%A")
                translator = Translator(to_lang="ru")
                dayWeekF = translator.translate(dayWeek)
                forecast += (str(dayWeekF) + "\n" +
                             translator.translate(str(location)) + "\n" +
                             "Температура: " + str(json_data['current']['temp']) + "°C\n" +
                             "Скорость ветра: " + str(json_data['current']['wind_speed']) + "м/с\n" +
                             "Давление: " + str(json_data['current']['pressure']) + "гПа\n" +
                             "Влажность: " + str(json_data['current']['humidity']) + "%\n" +
                             translator.translate(str(json_data['current']['weather'][0]['description'])))
                image = ""
                description = str(json_data['current']['weather'][0]['description'])
                await message.reply(forecast)
                if "clear" in description:
                        image = config.image_Clear
                elif "rain" in description:
                        image = config.image_Rain
                else:
                        image = config.image_Clouds

                await bot.send_photo(message.chat.id, image)


if __name__ == '__main__':
    executor.start_polling(dp)