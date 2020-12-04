import time
from pynput.keyboard import Key, Controller
text = open("text.txt", "r")
keyboard = Controller()
print("Program starting in 7 secs...")
time.sleep(7)
for x in text:
    keyboard.type(x)
    time.sleep(5)
