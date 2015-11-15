from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin

WIDTH, HEIGHT = 640, 480

window = Tk()
window.geometry('640x480')
canvas = Canvas(window, width=100, height=100, bg="#000000")
canvas.pack()


mainloop()