from Tkinter import *
from time import sleep
import sys

class HelloCallable:
    def __init__(self):
        self.msg = "Hello __call__ world"

    def __call__(self):
        print(self.msg)
        sleep(2)
        sys.exit()

widget = Button(None, text="Hello world Event", command=HelloCallable())
widget.pack(expand=YES)
widget.mainloop()
