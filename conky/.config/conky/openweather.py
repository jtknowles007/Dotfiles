#! /usr/bin/env python3
import pprint
import getjson as pm
import datetime as dt
import credentials

latitude = 40.03375
longitude = -85.67667
zipcode = 46013
weatherkey = credentials.mykey
symbol = "°"
symbol2 = "%"
path = "~/.config/conky/openweathericons/"
filetype = ".png"

today = dt.datetime.today()
todayindex = today.weekday()
weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
result = []
for i in range(5):
    next_index = (todayindex + i)%7
    result.append((weekdays[next_index]))

weatherurl = ("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid={}".format(latitude,longitude,weatherkey))
weatherdata = pm.getjson(weatherurl)
pprint.pprint(weatherdata)
current = round(weatherdata['main']['temp'])
icon = weatherdata['weather'][0]['icon']
iconpath = path + icon + filetype

forecasturl = ("https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&units=imperial&appid={}".format(latitude,longitude,weatherkey))
forecastdata = pm.getjson(forecasturl)
print(forecastdata)

forecast1 = round(forecastdata['list'][6]['main']['temp_min'])
forecast1b = round(forecastdata['list'][6]['main']['temp_max'])
icon1 = forecastdata['list'][6]['weather'][0]['icon']
iconpath1 = path+icon1+filetype

forecast2 = round(forecastdata['list'][14]['main']['temp'])
icon2 = forecastdata['list'][14]['weather'][0]['icon']
iconpath2 = path+icon2+filetype

forecast3 = round(forecastdata['list'][22]['main']['temp'])
icon3 = forecastdata['list'][22]['weather'][0]['icon']
iconpath3 = path+icon3+filetype

forecast4 = round(forecastdata['list'][30]['main']['temp'])
icon4 = forecastdata['list'][30]['weather'][0]['icon']
iconpath4 = path+icon4+filetype


print("${{image {} -p 24,237 -s 32x32}}".format(iconpath))
print("${{image {} -p 124,237 -s 32x32}}".format(iconpath1))
print("${{image {} -p 224,237 -s 32x32}}".format(iconpath2))
print("${{image {} -p 324,237 -s 32x32}}".format(iconpath3))
print("${{image {} -p 424,237 -s 32x32}}".format(iconpath4))
print("${{goto 60}}${{voffset -150}}${{font Monofur Nerd Font Mono:size=20}}{}{}${{goto 160}}{}{}/{}{}${{goto 260}}{}{}${{goto 360}}{}{}${{goto 460}}{}{}".format(current,symbol,forecast1,symbol,forecast1b,symbol,forecast2,symbol,forecast3,symbol,forecast4,symbol))
print("${{goto 32}}${{voffset -10}}${{font Monofur Nerd Font Mono:size=12}}Today${{goto 132}}{}${{goto 232}}{}${{goto 332}}{}${{goto 432}}{}${{font}}".format(result[1],result[2],result[3],result[4]))
