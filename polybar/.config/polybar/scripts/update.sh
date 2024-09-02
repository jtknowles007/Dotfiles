#! /usr/bin/env bash

UPDATES=$(apt-get upgrade -s |grep -P '^\d+ upgraded'|cut -d" " -f1)

if [ "$UPDATES" == "0" ]; then
    echo "$UPDATES"
else
    echo "%{F#66ff66}$UPDATES%{F-}"
fi

