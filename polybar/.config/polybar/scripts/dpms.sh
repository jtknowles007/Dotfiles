#! /usr/bin/env bash

DPMS_STATUS=$(xset q | grep "DPMS is" | awk '{print $3}')

if [ "$DPMS_STATUS" == "Enabled" ]; then
    echo " %{F#F37413}󰌪%{F-} "
else
    echo " %{F#CACACA}󰌪%{F-} "
fi
