from Tkinter import *
import sys

button1_text = Label(None, text="The only Button:")
button1_text.pack(expand=YES)
widget = Button(None, text="Click Here To exit", command=sys.exit)
widget.pack(expand=YES, fill=X)
widget.mainloop()
