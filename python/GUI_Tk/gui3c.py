from Tkinter import *
from time import sleep

def func(a, b):
    print(a**b)
    sleep(5)
    exit()

def callback():
    func(2, 5)
widget = Button(None, text="Click Me", command=callback)
widget.pack(expand=YES)
widget.mainloop()
