from tkinter import *

window = Tk()

photo = PhotoImage(file='cat.png')
count=0
def click():
    global count
    count +=1
    print("You Clicked!: ", count, " times")

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#04AF37",
                bg="#0000FF",
                activeforeground="#04AF37",
                activebackground="#0000FF",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()


window.mainloop()