from tkinter import * 

#grid() geometry manager



window = Tk()



firstName = Label(window, text="First name").grid(row=0, column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=0, column=1)

lastName = Label(window, text="last name").grid(row=1, column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=1, column=1)

email = Label(window, text="email").grid(row=2, column=0)
emailEntry = Entry(window)
emailEntry.grid(row=2, column=1)

def submits():
    fname = firstNameEntry.get()
    lname = lastNameEntry.get()
    mail = emailEntry.get()
    print("\n",fname , "\n", lname, "\n", mail
    ) 

submit = Button(window, text="submit", command=submits).grid(row=3, column=0, columnspan=2)


window.mainloop()