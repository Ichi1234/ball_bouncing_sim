import turtle
import random

class Balls:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls, speed):
        turtle.hideturtle()
        self.speed = turtle.speed(speed)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.color_list = []
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

        self.initilizing(canvas_width, canvas_height, ball_radius, num_balls)
    def draw_circle(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i],self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.speed("slowest")
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def move_circle(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def initilizing(self, canvas_width, canvas_height, ball_radius, num_balls):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(num_balls):
            self.xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            self.ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            self.vx.append(random.randint(1, 0.01*canvas_width))
            self.vy.append(random.randint(1, 0.01*canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        return self.xpos, self.ypos, self.vx, self.vy, self.ball_color