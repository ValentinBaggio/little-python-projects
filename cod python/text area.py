from tkinter import *

def submit():
    message = text.get("1.0", END)
    print(message)

window = Tk()

text = Text(window,
            bg="light blue",
            font=('Ink Free', 25),
            height=8,
            width=20,
            pady=15,
            padx=15)
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()