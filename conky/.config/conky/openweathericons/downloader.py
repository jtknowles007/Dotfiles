#! /usr/bin/env python3

import wget

iconcode = ['01d.png','02d.png','03d.png','04d.png','09d.png','10d.png','11d.png','13d.png','50d.png','01n.png','02n.png','03n.png','04n.png','09n.png','10n.png','11n.png','13n.png','50n.png']
url = 'https://openweathermap.org/img/wn/'


for i in iconcode:
    wget.download('https://openweathermap.org/img/wn/'+ i)

