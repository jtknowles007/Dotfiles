#!/usr/bin/env bash

polybar-msg cmd quit
# Nuclear Option if ipc not enabled
# killall -q polybar

echo "---" | tee -a /tmp/polybar1.log tmp/polybar2.log
polybar main 2>&1 | tee -a /tmp/polybar1.log & disown
polybar secondary 2>&1 | tee /tmp/polybar2.log & disown
polybar three 2>&1 | tee /tmp/polybar3.log & disown
