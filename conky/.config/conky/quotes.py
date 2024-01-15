#! /usr/bin/env python3

import json
import textwrap
from random import randint
with open('quotes.json','r') as file:
    data=json.load(file)
    res = sum(1 for i in data if type(i)==dict)
    value=randint(0,res)
movie = data[value]['quote']
source = data[value]['source']
quotewrap = textwrap.fill(movie,35)
sourcewrap = textwrap.fill(source,35)
print(quotewrap+"\n\n"+sourcewrap)
