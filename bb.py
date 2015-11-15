import pyscreenshot as img
import time
import win32api
import win32con


time.clock()
time.sleep(2)
image = img.grab()
for y in range(200, 500, 10):
    for x in range(800, 950, 10):
        # color = image.getpixel((x, y))
        # if color == (255, 3, 2):
            # print('red')
        win32api.SetCursorPos((y, x))
        print(y, x)
        time.sleep(0.01)
            # time.sleep(0.5)
        # print(color)
print(time.clock())
# image.show()