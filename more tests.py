from win32api import GetKeyState
import time


def keyIsUp(key):
    keystate = GetKeyState( key )
    if (keystate == 0) or (keystate == 1):
        return True
    else:
        return False


def keyIsDown(key):
    keystate = GetKeyState( key )
    if (keystate != 0) and (keystate != 1):
        return True
    else:
        return False


def f():
    while True:
        if keyIsDown(17):
            print('down')
            time.sleep(1)
        time.sleep(1)


f()
