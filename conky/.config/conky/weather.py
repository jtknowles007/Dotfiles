#! /usr/bin/env python3

import getjson as pm
import datetime as dt
import credentials

latitude = 40.05
longitude = -85.67
zipcode = 46013
weatherkey = credentials.mykey
symbol = "°"
symbol2 = "%"
path = "~/.config/conky/monoweathericons/"
filetype = ".png"

today = dt.datetime.today()
todayindex = today.weekday()
weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
result = []
for i in range(5):
    next_index = (todayindex + i)%7
    result.append((weekdays[next_index]))

weatherurl = ("https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid={}".format(zipcode,weatherkey))
weatherdata = pm.getjson(weatherurl)
current = round(weatherdata['main']['temp'])
icon = weatherdata['weather'][0]['icon']
iconpath = path + icon + filetype

forecasturl = ("https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=imperial&appid={}".format(latitude,longitude,weatherkey))
forecastdata = pm.getjson(forecasturl)
forecast1 = round(forecastdata['list'][2]['main']['temp'])
icon1 = forecastdata['list'][2]['weather'][0]['icon']
iconpath1 = path+icon1+filetype

forecast2 = round(forecastdata['list'][10]['main']['temp'])
icon2 = forecastdata['list'][10]['weather'][0]['icon']
iconpath2 = path+icon2+filetype

forecast3 = round(forecastdata['list'][18]['main']['temp'])
icon3 = forecastdata['list'][18]['weather'][0]['icon']
iconpath3 = path+icon3+filetype

forecast4 = round(forecastdata['list'][26]['main']['temp'])
icon4 = forecastdata['list'][26]['weather'][0]['icon']
iconpath4 = path+icon4+filetype


print("${{image {} -p 24,237 -s 32x32}}".format(iconpath))
print("${{image {} -p 124,237 -s 32x32}}".format(iconpath1))
print("${{image {} -p 224,237 -s 32x32}}".format(iconpath2))
print("${{image {} -p 324,237 -s 32x32}}".format(iconpath3))
print("${{image {} -p 424,237 -s 32x32}}".format(iconpath4))
print("${{goto 60}}${{voffset -150}}${{font TimeBurner:size=20}}{}{}${{goto 160}}{}{}${{goto 260}}{}{}${{goto 360}}{}{}${{goto 460}}{}{}".format(current,symbol,forecast1,symbol,forecast2,symbol,forecast3,symbol,forecast4,symbol))
print("${{goto 27}}${{voffset -10}}${{font TimeBurner:size=12}}{}${{goto 127}}{}${{goto 227}}{}${{goto 327}}{}${{goto 427}}{}${{font}}".format(result[0],result[1],result[2],result[3],result[4]))