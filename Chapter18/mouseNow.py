#! python3
#mouseNow.py - Displays the mouse cursor's current location 

import pyautogui

print('Press Crtl-C to quit.')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' +str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        

except KeyboardInterrupt:
           print('\nDone.')