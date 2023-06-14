from tkinter import *

food = ['pizza', 'hot dog', 'hamburger']


window = Tk()

pizza=PhotoImage(file='pizza.png')
hot_dog=PhotoImage(file='hotdog.png')
hamburger=PhotoImage(file='hamburger.png')

foodImages = [pizza, hot_dog, hamburger]

x = IntVar()

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered hot dog")
    elif(x.get()==2):
        print("you ordered hamburger")
    else:
        print("NAH!")

for i in range(len(food)):
    radio_button=Radiobutton(window, 
                             text=food[i], 
                             variable=x, 
                             value=i,
                             padx=25,
                             pady=10,
                             font=('Comic Sans', 20),
                             image=foodImages[i],
                             compound="right",
                             indicatoron=0,
                             width=100,
                             height=100,
                             command=order)
    radio_button.pack(anchor=W)

window.mainloop()