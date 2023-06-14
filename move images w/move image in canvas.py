from tkinter import *

def move_up(event):
   canvas.move(photo,0,-10)
def move_down(event):
   canvas.move(photo,0,10)
def move_left(event):
   canvas.move(photo,-10,0)
def move_right(event):
   canvas.move(photo,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

myImage = PhotoImage(file='C:\\Users\\Vaio\\Desktop\\python\\cod python\\fire.png')

photo = canvas.create_image(0,0, image=myImage, anchor=NW)

window.mainloop()