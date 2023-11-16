import turtle
from ball import Balls

class Simulation:

    def __init__(self):
        self.speed = turtle.speed("slowest")
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width


num_balls = int(input("Number of balls to simulate: "))
speed = int(input("Enter the speed for the balls: "))
turtle.tracer(0)
# turtle.speed(0)
# turtle.tracer(0)
# canvas_width = turtle.screensize()[0]
# canvas_height = turtle.screensize()[1]
# ball_radius = 0.05 * canvas_width
sim = Simulation()

ball = Balls(sim.canvas_width, sim.canvas_height, sim.ball_radius, num_balls, speed)
while True:
    turtle.clear()
    for i in range(num_balls):
        ball.draw_circle(i)
        ball.move_circle(i)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
