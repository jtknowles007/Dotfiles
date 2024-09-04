#!/usr/bin/env bash

ST=$(apt list --upgradable | awk -F"/" '{print $1}')
NU="Listing..."
if [ "$ST" = "$NU" ]; then
    ARR="Up to date"
else
    ARR=($ST)
fi

CHOICE=$(printf '%s\n' "${ARR[@]}" | rofi -dmenu -theme ~/.config/polybar/scripts/rofi/upd.rasi -p "")
