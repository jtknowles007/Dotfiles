#! /usr/bin/env python3
import getjson as pm
import datetime as dt
import textwrap
import credentials

weatherkey = credentials.weatherapi
zipcode = 46013
symbol = "°"
system = "F"
speed = "mph"
path = "~/.config/conky/weatherapicons/"
font = "${font IBM Plex Mono:size=12}"
font2 = "${font IBM Plex Mono:size=16}"
today = dt.datetime.today()
todayindex = today.weekday()
weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
result = []
for i in range(5):
    next_index = (todayindex + i)%7
    result.append((weekdays[next_index]))

forecasturl = ("https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=5&aqi=no&alerts=yes&hour=16".format(weatherkey,zipcode))
forecastdata = pm.getjson(forecasturl)
condition = textwrap.fill(str(forecastdata['current']['condition']['text']),10)
currenttemp = str(round(forecastdata['current']['temp_f'])) + symbol
feelslike = str(round(forecastdata['current']['feelslike_f'])) + symbol
lo = str(round(forecastdata['forecast']['forecastday'][0]['day']['mintemp_f'])) + symbol
hi = str(round(forecastdata['forecast']['forecastday'][0]['day']['maxtemp_f'])) + symbol
windspeed = str(round(forecastdata['current']['wind_mph'])) + speed
winddirection = forecastdata['current']['wind_dir']
windgust = str(round(forecastdata['current']['gust_mph'])) + speed
humidity = str(forecastdata['current']['humidity']) + "%"
precipitation = str(round(forecastdata['current']['precip_in'])) + "in"
clouds = str(forecastdata['current']['cloud']) + "%"
visibility = str(round(forecastdata['current']['vis_miles'])) + " mi"
sunrise = forecastdata['forecast']['forecastday'][0]['astro']['sunrise']
sunset = forecastdata['forecast']['forecastday'][0]['astro']['sunset']
moonrise = forecastdata['forecast']['forecastday'][0]['astro']['moonrise']
moonset = forecastdata['forecast']['forecastday'][0]['astro']['moonset']
rain = str(round(forecastdata['forecast']['forecastday'][0]['day']['totalprecip_in'],1)) + "\""

if len(forecastdata['alerts']['alert']) !=0:
    desc = forecastdata['alerts']['alert'][0]['desc']
    desc = desc.replace('\n',' ')
    desc = desc.replace(' * ','\n\n')
    desc = desc.replace('...','\n')
    myalert = open('alert.txt','w')
    myalert.write(desc)
    myalert.close
else:
    desc = ""
    myalert = open('alert.txt','w')
    myalert.write(desc)
    myalert.close
isday = forecastdata['current']['is_day']
icon = forecastdata['current']['condition']['icon']
if isday==1:
    daynight = "day/"
else:
    daynight = "night/"

icon = path + daynight + icon.rsplit('/',1)[1]

print("${{image {} -p 200,60 -s 100x100}}".format(icon))
print("${font IBM Plex Mono:size=12}${color1}WEATHER ${hr 1}${color}")
print("${{voffset 20}}${{font IBM Plex Mono:size=36}}{}{}".format(currenttemp,font))
print("${{voffset 30}}Feels like:${{offset 5}}{}${{goto 200}}Wind:${{offset 5}}{} {}".format(feelslike,winddirection,windspeed))
print("Hi/Lo:${{offset 5}}{}/{}${{goto 200}}Gusts:${{offset 5}}{}".format(hi,lo,windgust))
print("Precip:${{offset 5}}{}${{goto 200}}Clouds:${{offset 5}}{}".format(rain,clouds))
print("Humidity:${{offset 5}}{}${{goto 200}}Vis:${{offset 5}}{}".format(humidity,visibility))
print("")
print("${color1}ASTRONOMICAL ${hr 1}${color}")
print("Sunrise:${{offset 5}}{}".format(sunrise))
print("Sunset:${{offset 5}}{}".format(sunset))
print("Moonrise:${{offset 5}}{}".format(moonrise))
print("Moonset:${{offset 5}}{}".format(moonset))
