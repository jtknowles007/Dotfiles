#! /usr/bin/env python3
""" Read quotes from list and output to Conky """

from random import randint
import textwrap
import quoteslist

# Get list from quoteslist
QUOTE_LIST = quoteslist.thevar

# Iterate over dicts within the list; find how many are there,
# and generate a random number within the count of available quotes
RESULT = sum(1 for i in QUOTE_LIST if isinstance(i,dict))
INDEX=randint(0, RESULT)

# Variables
MOVIE_QUOTE = QUOTE_LIST[INDEX]['quote']
MOVIE_TITLE = QUOTE_LIST[INDEX]['source']
MOVIE_SPEAKER = QUOTE_LIST[INDEX]['speaker']
QUOTE_WRAP = textwrap.fill(MOVIE_QUOTE, 40)
TITLE_WRAP = textwrap.fill(MOVIE_TITLE, 40)
SPEAKER_WRAP = textwrap.fill(MOVIE_SPEAKER, 40)

# Output
print("${font IBM Plex Mono:size=10}" + QUOTE_WRAP + "\n\n" +
      SPEAKER_WRAP + "\n" + TITLE_WRAP)
