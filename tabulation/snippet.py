import random
import pyautogui as pg
import time

time.sleep(8)

for i in range(10):
    pg.write("hello")
    pg.press("enter")