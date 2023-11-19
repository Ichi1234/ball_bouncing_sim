import turtle
from ball import Balls
import random

class Simulation:

    def __init__(self):
        self.balls = []
        self.speed = 0
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def initilizing(self, ball_speed, ball_radius, num_balls):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + ball_radius, self.canvas_width - ball_radius))
            self.ypos.append(random.randint(-1 * self.canvas_height + ball_radius, self.canvas_height - ball_radius))
            self.vx.append(ball_speed)
            self.vy.append(ball_speed)
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.speed = ball_speed
            self.ball_radius = ball_radius
        return self.xpos, self.ypos, self.vx, self.vy, self.ball_color, self.speed, self.ball_radius

num_balls = int(input("Number of balls to simulate: "))
speed = int(input("Enter the speed for the balls: "))
size = int(input("Enter the size for the balls: "))
turtle.tracer(0)

sim = Simulation()

xpos, ypos, vx, vy, colors, speed_of_balls, size_of_balls = sim.initilizing(speed, size, num_balls)
ball = Balls(xpos, ypos, vx, vy, colors, speed_of_balls, size_of_balls)

while True:
    turtle.clear()
    for i in range(num_balls):
        b = ball.draw_circle(i)
        ball.move_circle(i)
        sim.balls.append(b)

    turtle.update()




