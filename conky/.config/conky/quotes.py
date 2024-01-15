#! /usr/bin/env python3

import json
import textwrap
from random import randint
with open('quotes.json','r') as fcc_file:
    fcc_data=json.load(fcc_file)
    res = sum(1 for i in fcc_data if type(i)==dict)
    value=randint(0,res)
movie = fcc_data[value]['quote']
source = fcc_data[value]['source']
quotewrap = textwrap.fill(movie,35)
sourcewrap = textwrap.fill(source,35)
print(quotewrap+"\n\n"+sourcewrap)
