def click():
    #messagebox.showinfo(title='This is an alert!', message="you are a robot")
    #messagebox.showwarning(title='This is an alert!', message="you are a robot")
    #messagebox.showerror(title='This is an alert!', message="you are a robot")

    #if messagebox.askokcancel(title="POST MORTEM", message="Do you want to listen post mortem?"):
     #   print("Go listen")
    #else:
     #   print("Are you sure?")

    #if messagebox.askretrycancel(title="POST MORTEM", message="Do you want to listen post mortem?"):
     #   print("Go listen")
    #else:
     #   print("Are you sure?")

    #if messagebox.askyesno(title="Ask yes or no?", message="do you like cake?"):
     #   print("I like cake too")
    #else:
     #   print("why do you not like cake?")
    
    #answer = messagebox.askquestion(title="Question:", message="Do you like pie?")
    #if(answer=="yes"):
     #   print("I like pie too")
    #else:
      #  print("Why you do not like pie?")

    answer = messagebox.askyesnocancel(title="Conditional", message="Do you like to code?", icon='warning')

    if(answer==True):
        print("You Like to code")
    elif(answer==False):
        print("you dont like coding")
    else:
        print("you have dodge the question")
    

from tkinter import *
from tkinter import messagebox


window = Tk()

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()