from Tkinter import *
from time import sleep
import sys

def greeting():
    print("I am trying to greet...")

win = Frame()
win.pack(side=TOP)
Button(win, text="Hello Button", command=greeting).pack(side=LEFT, anchor=N)
Label(win, text="Hello container world").pack(side=BOTTOM, anchor=SW)
Button(win, text="Quit Button", command=win.quit).pack(side=LEFT)

win.mainloop()
