#! /usr/bin/env python3

import getjson as pm
import datetime as dt

import credentials

weatherkey = credentials.weatherapi
zipcode = 46013
symbol = "°"
system = "F"
speed = "mph"
path = "~/.config/conky/weatherapicons/"
font = "${font IBM Plex Mono:size=12}"
font2 = "${font IBM Plex Mono:size=16}"

# Determine today and the next four days
today = dt.datetime.today()
todayindex = today.weekday()
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")
result = []

for i in range(5):
    next_index = (todayindex + i) % 7
    result.append((weekdays[next_index]))

# Query API and populate variables of interest
forecasturl = ("https://api.weatherapi.com/v1/forecast.json?key={}&q={} \
               &days=5&aqi=no&alerts=yes&hour=16".format(weatherkey, zipcode))

forecastdata = pm.getjson(forecasturl)
currenttemp = str(round(forecastdata['current']['temp_f'])) + symbol
feelslike = str(round(forecastdata['current']['feelslike_f'])) + symbol
lo = str(round(forecastdata['forecast']['forecastday'][0]['day']
               ['mintemp_f'])) + symbol
hi = str(round(forecastdata['forecast']['forecastday'][0]['day']
               ['maxtemp_f'])) + symbol

windspeed = str(round(forecastdata['current']['wind_mph'])) + speed
winddirection = forecastdata['current']['wind_dir']
windgust = str(round(forecastdata['current']['gust_mph'])) + speed

humidity = str(forecastdata['current']['humidity']) + "%"
rain = str(round(forecastdata['forecast']['forecastday'][0]['day']
                 ['totalprecip_in'], 1)) + "\""

clouds = str(forecastdata['current']['cloud']) + "%"
visibility = str(round(forecastdata['current']['vis_miles'])) + " mi"

isday = forecastdata['current']['is_day']
icon = forecastdata['current']['condition']['icon']

sunrise = forecastdata['forecast']['forecastday'][0]['astro']['sunrise']
sunset = forecastdata['forecast']['forecastday'][0]['astro']['sunset']
moonrise = forecastdata['forecast']['forecastday'][0]['astro']['moonrise']
moonset = forecastdata['forecast']['forecastday'][0]['astro']['moonset']

# Populate variables with 4 day forecast values
dayhi = []
daylo = []
dayicon = []

for i in range(1, 5):
    thevar = str(round(forecastdata['forecast']['forecastday']
                       [i]['day']['maxtemp_f'])) + symbol
    dayhi.append(thevar)

for i in range(1, 5):
    thevar = str(round(forecastdata['forecast']['forecastday']
                       [i]['day']['mintemp_f'])) + symbol
    daylo.append(thevar)

for i in range(1, 5):
    thevar = (forecastdata['forecast']['forecastday']
              [i]['day']['condition']['icon'])
    theicon = path + "day/" + thevar.rsplit('/', 1)[1]
    dayicon.append(theicon)

# Determine if there is an alert for today and send alert to a text file
# for alert.py script to handle.  If there are no alerts for today, clear
# the text file.

if len(forecastdata['alerts']['alert']) != 0:
    desc = forecastdata['alerts']['alert'][0]['desc']
    desc = desc.replace('\n', ' ')
    desc = desc.replace(' * ', '\n\n')
    desc = desc.replace('...', '\n')
    myalert = open('alert.txt', 'w')
    myalert.write("${color1}ALERTS ${hr 1}${color}${voffset -20}")
    myalert.write(desc)
    myalert.close
else:
    desc = ""
    myalert = open('alert.txt', 'w')
    myalert.write(desc)
    myalert.close

# Determine if it is day or night and select the appropriate icon set
if isday == 1:
    daynight = "day/"
else:
    daynight = "night/"

icon = path + daynight + icon.rsplit('/', 1)[1]

# Output to conky
#
# Weather Section
print("${font IBM Plex Mono:size=12}${color1}WEATHER ${hr 1}${color}")
print("${{image {} -p 200,60 -s 100x100}}".format(icon))

print("${{voffset 20}}${{font IBM Plex Mono:size=36}}{}{}"
      .format(currenttemp, font))

print(("${{voffset 30}}Feels like:${{offset 5}}{}${{goto 200}}Wind:"
      "${{offset 5}}{} {}").format(feelslike, winddirection, windspeed))

print("Hi/Lo:${{offset 5}}{}/{}${{goto 200}}Gusts:${{offset 5}}{}"
      .format(hi, lo, windgust))

print("Precip:${{offset 5}}{}${{goto 200}}Clouds:${{offset 5}}{}"
      .format(rain, clouds))

print("Humidity:${{offset 5}}{}${{goto 200}}Vis:${{offset 5}}{}"
      .format(humidity, visibility))
print("")

# Forecast Section
print("${font IBM Plex Mono:size=12}${color1}FORECAST ${hr 1}${color}")
print("${{image {} -p 0,310 -s 50x50}}${{image {} -p 95,310 -s 50x50}} \
      ${{image {} -p 190,310 -s 50x50}}${{image {} -p 285,310 -s 50x50}}"
      .format(dayicon[0], dayicon[1], dayicon[2], dayicon[3]))

print("${{font IBM Plex Mono:size=8}}${{voffset 30}}${{goto 2}}{} / {} \
      ${{goto 98}}{} / {}${{goto 190}}{} / {}${{goto 285}}{} / {}"
      .format(dayhi[0], daylo[0], dayhi[1], daylo[1], dayhi[2], daylo[2],
              dayhi[3], daylo[3]))

print("${{goto 5}}{}${{goto 105}}{}${{goto 197}}{}${{goto 290}}{}"
      .format(result[1], result[2], result[3], result[4]))

print("${font IBM Plex Mono:size=12}")

# Astronomical Section
print("${color1}ASTRONOMICAL ${hr 1}${color}")
print("Sunrise:${{offset 5}}{}".format(sunrise))
print("Sunset:${{offset 5}}{}".format(sunset))
print("Moonrise:${{offset 5}}{}".format(moonrise))
print("Moonset:${{offset 5}}{}".format(moonset))
