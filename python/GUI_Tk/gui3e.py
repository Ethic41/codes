from Tkinter import *
from time import sleep
import sys

def hello(event):
    print("Twice to exit")

def quit(event):
    print("Hello, I must be going...")
    sleep(2)
    sys.exit()

widget = Button(None, text="Hello Event")
widget.pack()
widget.bind("<Button-1>", hello)
widget.bind("<Double-1>", quit)
widget.mainloop()
a
