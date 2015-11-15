import pyscreenshot as img
import time
import win32api
import win32con
import msvcrt
import win32api
import win32con
import tkinter as tk
import threading


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        label = tk.Label(self.root, text="Left click on feathers")
        label.pack()
        self.root.configure(background='gold')
        self.root.lift()
        self.root.after(3000, self.callback)
        self.root.mainloop()


def get_cursor_position():
    App()
    pos = win32api.GetCursorPos()
    print(pos)


get_cursor_position()
