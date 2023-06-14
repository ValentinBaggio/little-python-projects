from tkinter import *

window = Tk() #instance of window
window.geometry("500x500")
window.title("Valentin Program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop()