import pyautogui
import time
import keyboard
import os
import threading
import cv2

time.sleep(1)
while True:
    try:
        x1, y1=pyautogui.center(pyautogui.locateOnScreen("image.png", confidence=0.75))
        time.sleep(1)
        pyautogui.moveTo(x1, y1)
        time.sleep(1)
        pyautogui.click(x1, y1, button='left')
        time.sleep(3)
    except:
        print(f'Первый скрипт не нашел. ')
        time.sleep(3)
    try:    
        x2, y2=pyautogui.center(pyautogui.locateOnScreen("image2.png", confidence=0.75))
        time.sleep(1)
        pyautogui.moveTo(x1, y1)
        time.sleep(1)
        pyautogui.click(x2, y2, button='left')
        time.sleep(3)
    except:
        print(f'Второй скрипт не нашел. ')
        time.sleep(3)