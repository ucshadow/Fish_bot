import pyscreenshot as img
import time
import msvcrt
import win32api
import win32con
import numpy as np
import tkinter as tk
import threading
import pyautogui
from win32api import GetKeyState
from ctypes import windll


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.cursor = 0
        self.color = 0
        self.color_now = 0
        self.title('SHADOW')
        self.geometry('600x300')

        self.x1 = tk.Label(self, text='first', width=20, anchor='w', fg='green')
        self.x2 = tk.Label(self, text='1', width=20, anchor='w', fg='magenta')
        self.b1 = tk.Button(text="Hello", command=self.b1_cb)
        self.x1.grid(row=0, column=0)
        self.x2.grid(row=0, column=1)
        self.b1.grid(row=0, column=3)

        self.e1 = tk.Label(self, text='bobbler color', width=20, anchor='w', fg='green')
        self.e2 = tk.Canvas(self, width=100, height=20, bg='yellow', relief='ridge')
        self.b2 = tk.Button(text='Get Color', command=self.color_thread)
        self.e1.grid(row=1, column=0)
        self.e2.grid(row=1, column=1)
        self.b2.grid(row=1, column=3)

        self.s1 = tk.Label(self, text='press to start', width=20, anchor='w', fg='green')
        self.s2 = tk.Canvas(self, width=100, height=20, bg='yellow', relief='ridge')
        self.b3 = tk.Button(text='Start Scan', command=self.loop_thread)
        self.s1.grid(row=2, column=0)
        self.s2.grid(row=2, column=1)
        self.b3.grid(row=2, column=3)

    def set_text(self, message):
        self.label.config(text=message)

    def b1_cb(self):
        # tk.messagebox.showinfo(str(self.rgb))
        print('bl_cl')

    def get_cursor_possition(self):
        cursor = win32api.GetCursorPos()
        self.cursor = cursor
        # print('cursor pos is ', self.cursor)
        return cursor

    def press_for_color(self):
        # print('ACTIVATED')
        while True:
            if self.key_down(17):
                pos = self.get_cursor_possition()
                hdc = windll.user32.GetDC(0)
                rgb = windll.gdi32.GetPixel(hdc, pos[0], pos[1])
                r = rgb & 0xff
                g = (rgb >> 8) & 0xff
                b = (rgb >> 16) & 0xff
                self.color = (r, g, b)
                # print('color is ', self.color)
                to_hex = ('#%02x%02x%02x' % (r, g, b))
                self.e2.config(bg=to_hex)
                self.b2.config(relief='raised')
                return 0
            time.sleep(0.1)

    def key_down(self, key):
        state = GetKeyState(key)
        if (state != 0) and (state != 1):
            return True
        else:
            return False

    def color_thread(self):
        self.b2.config(relief='sunken')
        th = threading.Thread(target=self.press_for_color)
        th.daemon = True
        th.start()

    def loop_thread(self):
        th = threading.Thread(target=self.start_scan)
        th.daemon = True
        th.start()

    def wait_thread(self):
        th = threading.Thread(target=self.waiting_for_fish)
        th.daemon = True
        th.start()

    def update_s2(self, c):
        self.s2.after(1000, lambda: self.s2.config(bg='#%02x%02x%02x' % c))

    def start_scan(self):
        # print(self.cursor, self.color)
        print('starting scan in 2')
        time.sleep(2)
        prev_position = [0, 0]
        while True:
            pyautogui.press('3')
            # time.sleep(1)
            color = self.color
            image = img.grab()
            for x in range(250, 1500, 2):             # change to fishing area
                for y in range(200, 650, 2):
                    color_now = image.getpixel((x, y))
                    if np.allclose(list(color_now), list(color), atol=10):
                        print('found color in position', x, y)
                        '''self.update_s2(color_now)
                        self.color_now = color_now
                        time.sleep(1)
                        win32api.SetCursorPos((x, y))
                        print('match!')
                        self.after(2000)'''
                        if abs(x - prev_position[0] >= 10) and abs(y - prev_position[2] >= 10):
                            prev_position[0] = x
                            prev_position[1] = y
                            win32api.SetCursorPos((x, y))
                            return self.wait_thread()
            print('scan Finished with no match...')

    def waiting_for_fish(self):
        time.clock()
        tolerance = t = 5
        while True:
            splash = (156, 150, 135)
            density = []
            image = img.grab()
            colors = set()
            cursor_position = win32api.GetCursorPos()
            x1, y1 = cursor_position[0], cursor_position[1]
            a = (x1 - 50, x1)
            b = (y1 - 25, y1 + 25)
            # time.clock()
            for x in range(a[0], a[1]):
                for y in range(b[0], b[1]):
                    # self.after(1, win32api.SetCursorPos((x, y)))
                    colors.add(image.getpixel((x, y)))
            for i in colors:
                if abs(splash[0] - i[0] <= t):
                    if abs(splash[1] - i[1] <= t):
                        if abs(splash[2] - i[2] <= t):
                            density.append(i)
            print('density length is', len(density))
            if len(density) > 100:
                pyautogui.rightClick()
                return self.start_scan()
            #print(time.clock())
            #print(colors)
            #print(len(colors))
            time.sleep(0.5)
            if time.clock() > 18:
                return self.start_scan()
        return self.start_scan()


app = App()
app.mainloop()

