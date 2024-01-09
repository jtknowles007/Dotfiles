#! /usr/bin/env python3
from PIL import Image
import requests
from bs4 import BeautifulSoup
import webbrowser
import re
moonphaseURL = 'https://www.moongiant.com/phase/today'
moonimages = '/home/john/.config/conky/north_moon/'
moonpage = requests.get(moonphaseURL)
moonsoup = BeautifulSoup(moonpage.content, "html.parser")
moontoday = moonsoup.find(id='today_')
moonsrc = moontoday.find_all("img")
for image in moonsrc:
    thevar = image['src']
thevar = moonimages+thevar[20:-4]+'.png'
#with Image.open(thevar) as img:
#    img.load()
#    img.show()
print("${{image {} -p 210,350 }}".format(thevar))
