#!/usr/bin/python3
# stopwatch.py - a simple stopwatch program

import time

# Display the program's instructions.
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Precc Ctrl-C to quit")
input() # Press enter to begin
print("Started.")
startTime = time.time() # Get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking lap times
try:
    while True:
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep the error message from displaying
    print('\nDone')
