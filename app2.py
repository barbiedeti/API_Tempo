import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "inserir chave api"

CITY = "Natal"

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&lang=pt"

response = requests.get(url).json()


temp_kelvin = response['main']['temp']
temp_celsius = round(kelvin_to_celsius(temp_kelvin))
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = round(kelvin_to_celsius(feels_like_kelvin))
humidity = response['main']['humidity']
description = response['weather'][0]['description'].title()

timezone_offset = response['timezone']
local_timezone = dt.timezone(dt.timedelta(seconds=timezone_offset))

sunrise_time_utc = dt.datetime.fromtimestamp(response['sys']['sunrise'])
sunset_time_utc = dt.datetime.fromtimestamp(response['sys']['sunset'])

sunrise_time_local = sunrise_time_utc.astimezone(local_timezone).strftime("%H:%M")
sunset_time_local = sunset_time_utc.astimezone(local_timezone).strftime("%H:%M")

print(f"Temperatura em {CITY}: {temp_celsius}°C")
print(f"Sensação térmica em {CITY}: {feels_like_celsius}°C")
print(f"Umidade em {CITY}: {humidity}%")
print(f"Clima Geral em {CITY}: {description}")
print(f"Nascer do Sol em {CITY}: {sunrise_time_local}")
print(f"Pôr do Sol em {CITY}: {sunset_time_local}")

