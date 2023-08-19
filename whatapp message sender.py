import pyautogui as xx
import time

# time.sleep(11)
xx.press("win")
time.sleep(2)
xx.typewrite("chrome")
xx.press("enter")
time.sleep(5)

xx.moveTo(800,500) #only if u have more than 3 account
xx.leftClick() #only if u have more than 3 account
time.sleep(2) #only if u have more than 3 account
xx.typewrite("https://web.whatsapp.com/")
xx.press("enter")
time.sleep(25)
xx.moveTo(100,182)

xx.leftClick()
xx.typewrite("my number")
xx.press("enter")
time.sleep(1)
for i in range(50):
    xx.typewrite(" yo")
    xx.press("enter")