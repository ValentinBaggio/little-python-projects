from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename() #muestra el camino hacia un archivo
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def openPath():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Vaio\\Desktop\\python\\dialog",
                                          title="Start in another directory",
                                          filetypes= (("text files", "*.txt"), 
                                                     ("all files", "*.*"))
                                                     )
    file = open(filepath, 'r')   #initialdir es donde arranca para abrir un archivo
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="Open File", command=openFile)
button.pack()

button = Button(window, text="Open Path", command=openPath)
button.pack()


window.mainloop()