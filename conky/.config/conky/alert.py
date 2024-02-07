#! /usr/bin/env python3
""" Import alert text from weatherapi and format for Conky """
import os
import sys
import textwrap

# Check if file exists and is empty.  If so, exit.
if os.path.isfile('alert.txt') and os.path.getsize('alert.txt') == 0:
    sys.exit()
# Open alert.txt file and read into variable
with open('alert.txt', 'r', encoding = 'utf-8') as MY_FILE:
    ALERT = MY_FILE.read()

# Split lines and determine position of items of interest
# within the list variable
MY_LINES = ALERT.splitlines()
MY_WHAT = MY_LINES.index('WHAT') + 1
MY_IMPACT = MY_LINES.index('IMPACTS') + 1

# Assign items of interest to variables
WHAT_TEXT = MY_LINES[MY_WHAT]
IMPACT_TEXT = MY_LINES[MY_IMPACT]

# Assign alert title to variable
TITLE = textwrap.fill(MY_LINES[1], width=35)

# Join items of interest into one text block and wrap text
# to fit conky window
FULL_LIST = []
FULL_LIST.append(WHAT_TEXT)
FULL_LIST.append(IMPACT_TEXT)

MERGED_TEXT = " ".join(str(element) for element in FULL_LIST)
WRAPPED_TEXT = textwrap.fill(MERGED_TEXT, width=35)

# Output to Conky
print(MY_LINES[0] + "\n")
print(TITLE + "\n")
print(WRAPPED_TEXT)
