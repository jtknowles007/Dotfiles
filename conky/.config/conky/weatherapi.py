#! /usr/bin/env python3
""" Receives weather report from weatherapi and formats output for Conky"""
import datetime as dt
import getjson as pm

import credentials

WEATHER_KEY = credentials.weatherapi
ZIPCODE = 46013
SYMBOL = "°"
SYSTEM = "F"
SPEED = "mph"
PATH = "~/.config/conky/weatherapicons/"

# Determine today and the next four days
TODAY = dt.datetime.today()
TODAY_INDEX = TODAY.weekday()
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")
RESULT = []

for i in range(5):
    NEXT_INDEX = (TODAY_INDEX + i) % 7
    RESULT.append((WEEKDAYS[NEXT_INDEX]))

# Query API and populate variables of interest
FORECAST_URL = "https://api.weatherapi.com/v1/forecast.json?key={}&q={} \
        &days=3&aqi=no&alerts=yes&hour=16".format(WEATHER_KEY, ZIPCODE)


FORECAST_DATA = pm.getjson(FORECAST_URL)
CURRENT_TEMP = str(round(FORECAST_DATA['current']['temp_f'])) + SYMBOL
FEELS_LIKE = str(round(FORECAST_DATA['current']['feelslike_f'])) + SYMBOL
LO_TEMP = str(round(FORECAST_DATA['forecast']['forecastday'][0]['day']
               ['mintemp_f'])) + SYMBOL
HI_TEMP = str(round(FORECAST_DATA['forecast']['forecastday'][0]['day']
               ['maxtemp_f'])) + SYMBOL

WIND_SPEED = str(round(FORECAST_DATA['current']['wind_mph'])) + SPEED
WIND_DIRECTION = FORECAST_DATA['current']['wind_dir']
WIND_GUST = str(round(FORECAST_DATA['current']['gust_mph'])) + SPEED

HUMIDITY= str(FORECAST_DATA['current']['humidity']) + "%"
RAIN = str(round(FORECAST_DATA['forecast']['forecastday'][0]['day']
                 ['totalprecip_in'], 1)) + "\""

CLOUDS = str(FORECAST_DATA['current']['cloud']) + "%"
VISIBILITY = str(round(FORECAST_DATA['current']['vis_miles'])) + " mi"

IS_DAY = FORECAST_DATA['current']['is_day']
ICON = FORECAST_DATA['current']['condition']['icon']

SUNRISE = FORECAST_DATA['forecast']['forecastday'][0]['astro']['sunrise']
SUNSET = FORECAST_DATA['forecast']['forecastday'][0]['astro']['sunset']
MOONRISE = FORECAST_DATA['forecast']['forecastday'][0]['astro']['moonrise']
MOONSET = FORECAST_DATA['forecast']['forecastday'][0]['astro']['moonset']

# Populate variables with 2 day forecast values
DAY_HI = []
DAY_LO = []
DAY_ICON = []

for i in range(1, 3):
    MAX_TEMP = str(round(FORECAST_DATA['forecast']['forecastday']
                        [i]['day']['maxtemp_f'])) + SYMBOL
    DAY_HI.append(MAX_TEMP)

for i in range(1, 3):
    MIN_TEMP = str(round(FORECAST_DATA['forecast']['forecastday']
                        [i]['day']['mintemp_f'])) + SYMBOL
    DAY_LO.append(MIN_TEMP)

for i in range(1, 3):
    FULL_ICON = (FORECAST_DATA['forecast']['forecastday']
              [i]['day']['condition']['icon'])
    NEW_ICON = PATH + "day/" + FULL_ICON.rsplit('/', 1)[1]
    DAY_ICON.append(NEW_ICON)

# Determine if there is an alert for TODAY and send alert to a text file
# for alert.py script to handle.  If there are no alerts for today, clear
# the text file.

if len(FORECAST_DATA['alerts']['alert']) != 0:
    ALERT_DESCRIPTION = ""
    ALERT_DESCRIPTOIN = FORECAST_DATA['alerts']['alert'][0]['desc']
    ALERT_DESCRIPTION = ALERT_DESCRIPTION.replace('\n', ' ')
    ALERT_DESCRIPTION = ALERT_DESCRIPTION.replace(' * ', '\n\n')
    ALERT_DESCRIPTION = ALERT_DESCRIPTION.replace('...', '\n')

    with open('alert.txt', 'w', encoding='utf-8') as MY_FILE:
        MY_FILE.write("${color1}ALERTS ${hr 1}${color}${voffset -20}")
        MY_FILE.write(ALERT_DESCRIPTION)
else:
    ALERT_DESCRIPTION = ""
    with open('alert.txt', 'w', encoding='utf-8') as MY_FILE:
        MY_FILE.write(ALERT_DESCRIPTION)

# Determine if it is day or night and select the appropriate ICON set
if IS_DAY == 1:
    DAY_NIGHT = "day/"
else:
    DAY_NIGHT = "night/"

ICON = PATH + DAY_NIGHT + ICON.rsplit('/', 1)[1]

# Output to conky
#
# Weather Section
print("${font IBM Plex Mono:size=12}${color1}WEATHER ${hr 1}${color}")
print("${{image {} -p 200,60 -s 100x100}}".format(ICON))

print("${{voffset 20}}${{font IBM Plex Mono:size=36}}{} \
      ${{font IBM Plex Mono:size=12}}".format(CURRENT_TEMP))

print(("${{voffset 30}}Feels like:${{offset 5}}{}${{goto 200}}Wind:"
      "${{offset 5}}{} {}").format(FEELS_LIKE, WIND_DIRECTION, WIND_SPEED))

print("Hi/Lo:${{offset 5}}{}/{}${{goto 200}}Gusts:${{offset 5}}{}"
      .format(HI_TEMP, LO_TEMP, WIND_GUST))

print("Precip:${{offset 5}}{}${{goto 200}}CLOUDS:${{offset 5}}{}"
      .format(RAIN, CLOUDS))

print("Humidity:${{offset 5}}{}${{goto 200}}Vis:${{offset 5}}{}"
      .format(HUMIDITY, VISIBILITY))
print("")

# Forecast Section
print("${font IBM Plex Mono:size=12}${color1}FORECAST ${hr 1}${color}")
print("${{image {} -p 0,315 -s 80x80}}${{image {} -p 175,315 -s 80x80}}"
      .format(DAY_ICON[0], DAY_ICON[1]))
print("${{goto 75}}{}${{goto 250}}{}".format(RESULT[1], RESULT[2]))
print("${{voffset 0}}${{goto 65}} {} / {}${{goto 250}}{} / {}"
      .format(DAY_HI[0], DAY_LO[0], DAY_HI[1], DAY_LO[1]))
print("\n")

# Astronomical Section
print("${color1}ASTRONOMICAL ${hr 1}${color}")
print("Sunrise:${{offset 5}}{}".format(SUNRISE))
print("Sunset:${{offset 5}}{}".format(SUNSET))
print("Moonrise:${{offset 5}}{}".format(MOONRISE))
print("Moonset:${{offset 5}}{}".format(MOONSET))
