import sys
from Tkinter import *
from time import sleep

def quit():
    return "Nothing Is True"
    sleep(5)
    sys.exit()

widget = Button(None, text="Click and See", command=quit)
widget.pack(expand=YES)
widget.mainloop()
