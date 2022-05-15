import time

from pynput.mouse import Button, Controller
from pynput import keyboard
import cv2 as cv
from matplotlib import pyplot as plt

mouse = Controller()

img = cv.imread('img.png')
img = cv.resize(img, (620, 340), interpolation=cv.INTER_AREA)
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 255, 0), 1)
# cv.imshow('gray', imgray)
# cv.imshow('thresh', img)
cv.imshow('image', img)


def getCords(point):
    return (point[0][0], point[0][1])

def move(cords):
    mouse.position = (560 + cords[0], 300 + cords[1])
    time.sleep(0.01)

def on_press(key):
    global buffer;
    buffer = key;


listener = keyboard.Listener(on_press=on_press)
listener.start()

time.sleep(5)

for contour in contours:
    move(getCords(contour[0]))
    mouse.press(Button.left)
    for point in contour:
        move(getCords(point))
    move(getCords(contour[0]))
    mouse.release(Button.left)

# while 1:
#     while(buffer != keyboard.KeyCode(char='1')):
#         time.sleep(0.01)
#     for contour in contours:
#         move(getCords(contour[0]))
#         mouse.press(Button.left)
#         for point in contour:
#             if buffer != keyboard.KeyCode(char='1'):
#                 break
#             move(getCords(point))
#         move(getCords(contour[0]))
#         mouse.release(Button.left)


cv.waitKey(0)


