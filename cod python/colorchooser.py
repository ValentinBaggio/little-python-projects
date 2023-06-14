def click():
    window.config(bg=colorchooser.askcolor()[1])

from tkinter import *
from tkinter import colorchooser

window = Tk()
window.geometry("500x500")
button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()