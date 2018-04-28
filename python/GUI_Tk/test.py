from Tkinter import *
from time import sleep
import sys
"""
class Application(Frame):
    def say_hi(self):
        print("hi there everyone")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
"""
"""
class SomeGuiClass:
    def __init__(self):
        self.x = 12
        self.y = 5
        widget = Button(None, text="Click Me", command=self.handler)
        widget.pack(fill=X, expand=YES)

    def handler(self):
        print(self.x * self.y)
        sleep(3)
        sys.exit()

SomeGuiClass()
mainloop()
"""
import tkMessageBox
#from Tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.frame = Frame(self.root, width=320, height=200,
                           borderwidth=2, relief=RAISED)
        self.frame.pack_propagate(False)
        self.frame.pack()
        self.bQuit = Button(self.frame, text="Quit",
                            command=self.root.quit)
        self.bQuit.pack(pady=20)
        self.bHello = Button(self.frame, text="Hello",
                             command=self.hello)
        self.bHello.pack(pady=20)

    def hello(self):
        tkMessageBox.showinfo("Popup", "Hello!")

app = App()
app.root.mainloop()
