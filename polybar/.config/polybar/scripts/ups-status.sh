#!/bin/bash

UPS="ec850@localhost"
status=$(upsc "$UPS" ups.status 2>/dev/null)
charge=$(upsc "$UPS" battery.charge 2>/dev/null)
runtime=$(upsc "$UPS" battery.runtime 2>/dev/null)
load=$(upsc "$UPS" ups.load 2>/dev/null)

# Convert seconds to minutes 
minutes=$((runtime / 60))
wattage=$((load * 510/100))

if [[ "$status" == *"OB"* ]]; then
    icon=""
elif [[ "$status" == *"OL"* ]]; then
    icon=""
else
    icon=""
fi

echo " PWR SRC ${icon} |  ${wattage}W |  ${charge}% |  ${minutes} min "
