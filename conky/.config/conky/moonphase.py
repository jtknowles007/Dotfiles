#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
moonphaseURL = 'https://www.moongiant.com/phase/today'
moonimages = '/home/john/.config/conky/north_moon/'
moonpage = requests.get(moonphaseURL)
moonsoup = BeautifulSoup(moonpage.content, "html.parser")
moontoday = moonsoup.find(id='today_')
moonsrc = moontoday.find_all("img")
for image in moonsrc:
    thevar = image['src']
thevar = moonimages + thevar[20:-4] + '.png'
print("${{image {} -p 225,450 -s 60x60}}".format(thevar))
