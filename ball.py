from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
        super().__init__()
        self.initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
        self.hideturtle()

        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []




    def draw_circle(self, color, size, x, y):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        self.penup()
        self.color(color)
        self.fillcolor(color)
        self.goto(x,y)
        self.pendown()
        self.begin_fill()
        self.circle(size)
        self.end_fill()

    def move_circle(self, i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        xpos[i] += vx[i]
        ypos[i] += vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
            vx[i] = -vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
            vy[i] = -vy[i]

    def initilizing(self, xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(num_balls):
            self.xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            self.ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            self.vx.append(random.randint(1, 0.01*canvas_width))
            self.vy.append(random.randint(1, 0.01*canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
