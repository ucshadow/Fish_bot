import win32api
from ctypes import windll
import numpy as np
import time
import pyscreenshot as img
from scipy import misc
import numpy
import cv2

'''time.clock()


image = img.grab()

for x in range(250, 1500, 2):             # change to fishing area
    for y in range(200, 650, 1):
        color_now = image.getpixel((x, y))

print(time.clock())'''


im = cv2.imread('1.jpg', 0)

cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()