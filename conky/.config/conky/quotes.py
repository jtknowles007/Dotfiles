#! /usr/bin/env python3

import quoteslist
from random import randint
import textwrap

# Get list from quoteslist
quotevar = quoteslist.thevar

# Iterate over dicts within the list; find how many are there,
# and generate a random number within the count of available quotes
res = sum(1 for i in quotevar if type(i)==dict)
value=randint(0,res)

# Variables
movie = quotevar[value]['quote']
source = quotevar[value]['source']
quotewrap = textwrap.fill(movie,40)
sourcewrap = textwrap.fill(source,40)

# Output
print("${font IBM Plex Mono:size=10}" + quotewrap+"\n\n"+sourcewrap)
