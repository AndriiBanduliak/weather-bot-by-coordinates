
import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(lat,lon, open_weather_token):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drezzle": "Drizzle\U00002614",
        "Thunderstorm": "Thundershtorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist\U0001F32B"
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look into the window I do not understand what the weather is "

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(
            f"погода в городе {city}\nТемпература :{cur_weather}C {wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\n Ветер: {wind}м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
            f"Have a nice day :) "
        )



    except Exception as ex:
        print(ex)
        print("Check the name of the city ")

def main():
    lat = input(' введите широту ')
    lon = input(" введите долготу ")
    get_weather(lat, lon, open_weather_token)

if __name__ == '__main__':
    main()

