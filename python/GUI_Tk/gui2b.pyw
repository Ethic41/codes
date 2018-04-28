from Tkinter import *

root = Tk()
Button(root, text="Left sided button", command=root.quit).pack(side=LEFT, expand=YES)
mainloop()
