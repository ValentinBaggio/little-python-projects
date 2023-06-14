


def submit():
    
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You have ordered: ")

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#F7FFDE',
                  font=("Constatia", 15),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"spaghetti")
listbox.insert(3,"carbonara pasta")
listbox.insert(4,"lobster")
listbox.insert(5,"hamburger")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window, text="submit",command=submit)
submit_button.pack()

add_button = Button(window, text="add",command=add)
add_button.pack()

delete_button = Button(window, text="delete",command=delete)
delete_button.pack()

window.mainloop()