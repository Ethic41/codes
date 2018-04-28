from Tkinter import *

root = Tk()
widget = Label(root)
widget.config(text="Hello, GUI world!....")
widget.pack(side=TOP, fill=BOTH, expand=YES)
root.title("hello")
root.mainloop()
