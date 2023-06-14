from tkinter import *

window = Tk()
window.geometry("500x500")
photo = PhotoImage(file='cat.png')

label = Label(  window, 
                text="Hello world", 
                font=('Arial', 40, 'bold'), 
                fg='green', 
                bg='blue',
                relief=RAISED,
                bd=10,
                padx=20,
                pady=20,
                image=photo,
                compound='top')
label.pack()

window.mainloop()