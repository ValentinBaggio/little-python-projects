from tkinter import *

window = Tk()

entry = Entry(window,
              font=('Arial', 20),
              bg="blue",
              fg="#00FF00",
              show="*", #PARA PONER DE EJEMPLO CONTRASEÑAS O COSAS ASI
              )
entry.insert(0, 'BOB')
entry.pack(side=LEFT)

def submit():
    username = entry.get()
    print(username)
   # entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)
    
def bacskpace():
    entry.delete(len(entry.get())-1, END)

submit_button= Button(window,
                      text="submit",
                      command=submit)
submit_button.pack(side=RIGHT)

delete_button= Button(window,
                      text="delete",
                      command=delete)
delete_button.pack(side=RIGHT)

backspace_button= Button(window,
                      text="backspace",
                      command=bacskpace)
backspace_button.pack(side=RIGHT)

window.mainloop()