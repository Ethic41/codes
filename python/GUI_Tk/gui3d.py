from Tkinter import *
import sys
from time import sleep


class HelloClass:
    def __init__(self):
        widget = Button(None, text="Click To Exit", command=self.quit)
        widget.pack(expand=YES, fill=X)

    def quit(self):
        print("Closing HelloClass")
        sleep(3)
        sys.exit()

HelloClass()
mainloop()
