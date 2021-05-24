import random
from settings import *

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score 

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 250)

        starts = [-2, -1, 1, 2]

        random.shuffle(starts)

        self.x = starts[0]
        self.y = -2 

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] > paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                
                self.score.add_point()
                return True

        return False

    def draw(self, color_end_text):
        self.canvas.move(self.id, self.x , self.y)

        pos = self.canvas.coords(self.id )

        if pos[1] <= 0:
            self.y = 2 

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

            self.canvas.create_text(250, 120, text="Game over :(", font=('Courier', 30), fill=color_end_text)

        if self.hit_paddle(pos) == True:
            self.y = -2 

        if pos[0] <= 0: 
            self.x = 2 

        if pos[2] >= self.canvas_width:
            self.x = -2 


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color ) 

        starts_1 = [40,60,120,150,180,200]

        random.shuffle(starts_1) 

        self.start_pos_x = starts_1[0]
        self.canvas.move(self.id, self.start_pos_x, 300)

        self.x = 0 
        self.canvas_width = self.canvas.winfo_width()

        self.game_started = False

        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)

        self.canvas.bind_all("<KeyPress-Return>", self.start_game)

    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def start_game(self, event):
        self.game_started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(450,10, text=self.score, font=('Courier', 20), fill=color)

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)