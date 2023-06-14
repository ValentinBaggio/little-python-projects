from tkinter import *
import time
from ball import *

WIDTH = 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0, 100, 1,1, "white")

tenis_ball = Ball(canvas, 0,0, 50, 5,3, "light green")

basket_ball = Ball(canvas, 0,0, 150, 2,3, "orange")

futbol_ball = Ball(canvas, 0,0, 125, 2,1, "grey")

while True:
    tenis_ball.move()
    volley_ball.move()
    basket_ball.move()
    futbol_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()