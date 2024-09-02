#!/usr/bin/env bash

ST=$(apt list --upgradable | awk -F"/" '{print $1}')
NU="Listing..."
if [ "$ST" = "$NU" ]; then
    ARR="Up to date"
else
    ARR=($ST)
    ARR+=("UPGRADE")
fi

CHOICE=$(printf '%s\n' "${ARR[@]}" | rofi -dmenu -theme ~/.config/polybar/scripts/rofi/upd.rasi -p "")

if [ "$CHOICE" = "UPGRADE" ]; then
    upgrade
    exit 0
fi

