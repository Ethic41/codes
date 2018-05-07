#CodeName: coreGUI.py
#Author: Dahir Muhammad Dahir
#Date: 05th-May-2018
#About: codes from the GUI chapter in core python text[Wesely Chan]

from Tkinter import *


def main():
	#tkhello()
	#buttonWidget()
	#buttonWithLabel()
	combined()

def tkhello():
	top = Tk()
	label = Label(top, text="Hello, GUI World...")
	label.pack()
	top.title("Hello")
	mainloop()


def buttonWidget():
	top = Tk()
	quit = Button(top, text="Exit Here", command=top.quit)
	top.title("Button")
	quit.pack(fill=X, expand=1)
	mainloop()


def buttonWithLabel():
	top = Tk()
	top.title("ButtonWithLabel")
	helloText = Label(top, text="Hello, Click the Button Below\nTo Exit")
	helloText.pack()
	quit = Button(top, text="Click To Exit", command=top.quit, bg="red", fg="white")
	quit.pack()
	mainloop()

def combined():
	top = Tk()
	top.title("Combined_Window")
	top.geometry("250x150")
	welcomeLabel = Label(top, text="Hello, Welocme to the combined window\nit is nice to have you here", font="Helvetica -12 bold")
	welcomeLabel.pack(fill=Y, expand=True)
	
	mainloop()


def combinedResize(ev=None):
	label.config(font="Helvetica -%d bold"%(scale.get()))


if __name__ == '__main__':
	main()
