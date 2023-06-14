from tkinter import *
from tkinter import filedialog

def save():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Vaio\\Desktop\\python\\dialog",
                                    defaultextension='.txt',
                                    filetypes= [
                                        ("Text file", ".txt"),
                                        ("HTML", ".html"),
                                        ("Stylesheet", ".css"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return                                     
    #filetext = str(text.get(1.0,END))
    filetext = input("Enter some text")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text="Save", command=save)
button.pack()

text = Text(window)
text.pack()

window.mainloop()