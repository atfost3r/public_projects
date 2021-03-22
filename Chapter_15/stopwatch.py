#! python3

#stopwatch.py - A simple stopwatch program

import time

#Display the program's instructions
print('Press ENTER to begin. Afterwards, press enter to "click" the stopwatch. Press CTRL-C to quit.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

#Start Tracking laps
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone')
    