from tkinter import *

def openFile():
    print("file has been opened")
def saveFile():
    print("file has been saved")

def cutText():
    print("file has been saved")
def copyText():
    print("file has been saved")
def pasteText():
    print("file has been saved")

# image = PhotoImage(file='photo')

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('Ink Free', 10))
menubar.add_cascade(label="file", menu=fileMenu)
fileMenu.add_command(label="open", command= openFile, 
                     #image=photo to add a photo, compound='direction'
                     )
fileMenu.add_command(label="save", command= saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="exit", command= exit)

editMenu = Menu(menubar, tearoff=0, font=('Ink Free', 10))
menubar.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="cut", command= cutText)
editMenu.add_command(label="copy", command= copyText)
editMenu.add_command(label="paste", command= pasteText)

window.mainloop()