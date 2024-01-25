#! /usr/bin/env python3
import textwrap

myalert = open('alert.txt','r')
alert = myalert.read()
myalert.close
mylines = alert.splitlines()
title = textwrap.fill(mylines[1],width=35)
fullist = []
fullist.append(mylines[5])
fullist.append(mylines[14])
fullist.append(mylines[17])
merged_fullist = " ".join(str(element) for element in fullist)
wrapped_text = textwrap.fill(merged_fullist,width=35)

print("${font IBM Plex Mono:size=12}")
print(title + "\n")
print(wrapped_text)
