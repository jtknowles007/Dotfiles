#! /usr/bin/env python3
import textwrap

# Open alert.txt file and read into variable
myalert = open('alert.txt','r')
alert = myalert.read()
myalert.close

# Split lines and determine position of items of interest within the list variable
mylines = alert.splitlines()
what = mylines.index('WHAT')+1
impact = mylines.index('IMPACTS')+1

# Assign items of interest to variables
whattext = mylines[what]
impacttext = mylines[impact]

# Assign alert title to variable
title = textwrap.fill(mylines[1],width=35)

# Join items of interest into one text block and wrap text to fit conky window 
fullist = []
fullist.append(whattext)
fullist.append(impacttext)

mergedtext = " ".join(str(element) for element in fullist)
wrappedtext = textwrap.fill(mergedtext,width=35)

# Output to Conky
print(mylines[0]+"\n")
print(title + "\n")
print(wrappedtext)
