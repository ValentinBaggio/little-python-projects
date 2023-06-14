from tkinter import *

def doSomething(event):
    print("thing in:", event.x, " ",event.y #event.x/y to see where is the event occurring
    )

window = Tk()

#window.bind("<Button-1>", doSomething) #left click Button-1
#window.bind("<Button-2>", doSomething) scroll click Button-2
#window.bind("<Button-3>", doSomething) right click Button-3
#window.bind("<ButtonRelease>", doSomething) #all but holding
#window.bind("<Enter>", doSomething)
#window.bind("<Leave>", doSomething)
window.bind("<Motion>", doSomething)

window.mainloop()