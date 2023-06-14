from tkinter import *

def submit():
    print("The temperature is: ", scale.get() , " degrees Celsius")  #con las comas evitas usar conversores tipo str()

window = Tk()


fire_photo = PhotoImage(file='fire.png')
fire_label = Label(image=fire_photo)
fire_label.pack()

ice_photo = PhotoImage(file='ice.png')
ice_label = Label(image=ice_photo)
ice_label.pack()

scale = Scale(window,
              from_=100, 
              to=0,
              length=400,
              width=300,
              orient=VERTICAL,
              font=('Comic Sans', 20),
              tickinterval=10, #añade intervalos
              #showvalue=0, #esconde el numero actual
              resolution=5, #cuanto se mueve la barrita
              troughcolor='#AA07BE',
              fg='#43AB57')
scale.pack()

scale.set(((scale['from']-scale['to'])/2)+scale['to'])



button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()