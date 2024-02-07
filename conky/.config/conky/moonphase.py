#! /usr/bin/env python3
""" Get current phase of moon and output corresponding image to Conky """

import requests
from bs4 import BeautifulSoup

MOON_PHASE_URL = 'https://www.moongiant.com/phase/today'
MOON_IMAGES = '/home/john/.config/conky/moonicons/'
MOON_PAGE = requests.get(MOON_PHASE_URL, timeout=15)
MOON_SOUP = BeautifulSoup(MOON_PAGE.content, "html.parser")
MOON_TODAY = MOON_SOUP.find(id='today_')
MOON_SOURCE = MOON_TODAY.find_all("img")
for MOON_IMG in MOON_SOURCE:
    MOON_PHASE = MOON_IMG['src']
MOON_PHASE = MOON_IMAGES + MOON_PHASE[20:-4] + '.png'
print("${{image {} -p 225,450 -s 60x60}}".format(MOON_PHASE))
