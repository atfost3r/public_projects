#! python3

#countdown.py - A Simple Countdown script

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end= '\n')
    time.sleep(1)
    timeLeft = timeLeft - 1

#Play sound file at the end of the program
subprocess.Popen(['start', 'C:\\Windows\\Media\\Alarm01.wav'], shell=True)