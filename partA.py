# Justin Brochu
# 11/1/25
# P4Lab1
# while and for loops to draw

import turtle

win = turtle.Screen()
marker = turtle.Turtle()

marker.pensize(6)
marker.color("red")
marker.shape("turtle")

for side in range(4):
    marker.forward(200)
    marker.left(90)

sides = 3

while sides > 0:
    marker.forward(200)
    marker.left(120)
    sides =sides - 1

win.mainloop()
