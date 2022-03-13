import pyautogui
import time

while(True):
    try:
        acc = pyautogui.locateOnScreen('accept.png', confidence=.7)
        acc_co = pyautogui.center(acc)
        x, y = acc_co.x, acc_co.y
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
    except:
        time.sleep(1)