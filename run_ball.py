import turtle
from ball import Ball


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
# turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
color_list = []
xpos = []
ypos = []
vx = []
vy = []
ball_color = []
balls = Ball(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls)
while True:
    turtle.clear()
    for i in range(num_balls):
        balls.draw_circle(ball_color[i], ball_radius, xpos[i], ypos[i])
        balls.move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
