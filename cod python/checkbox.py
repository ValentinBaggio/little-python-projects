from tkinter import *

window = Tk()

photo = PhotoImage(file='cat.png')

x = IntVar() #si los valores de onvalue y offvalue son 
             #booleanos hay que reemplazar IntVar() por BooleanVar()


def display():
    if(x.get()==1): #se borraria el ==1
        print("You agree")
    else:
        print("you dont agree")

check_button = Checkbutton(window,
                           text="i agree something",
                           variable=x,
                           onvalue=1, #puede ser 1 o True
                           offvalue=0, #puede ser 0 o False
                           command=display,
                           font=('Arial', 20),
                           fg="#AB34DE",
                           bg="#FF47ED",
                           activebackground="#FF47ED",
                           activeforeground="#AB34DE",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound="left")
check_button.pack(side=RIGHT)

window.mainloop()