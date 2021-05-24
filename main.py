from tkinter import *
import time

from settings import *
from objects import *

tk = Tk()

tk.title(GAME_NAME)
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=WIDHT, height=HEIGHT, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, COLOR_PADLE)
score = Score(canvas, COLOR_SCORE)
ball = Ball(canvas, paddle, score, COLOR_BALL)


while not ball.hit_bottom:

    if paddle.game_started == True:
        ball.draw(COLOR_END_TEXT)
        paddle.draw()

    tk.update_idletasks()
    tk.update()

    time.sleep(0.01)

time.sleep(3)
