# Justin Brochu
# 11/1/25
# P4Lab1 part B
# drawing initials

import turtle

win = turtle.Screen()
marker = turtle.Turtle()

marker.pensize(6)
marker.color("red")
marker.shape("turtle")

marker.forward(100)
marker.back(50)
marker.right(90)
marker.forward(100)
marker.right(90)
marker.forward(50)
marker.right(90)
marker.forward(25)

marker.penup()
marker.goto(150,0)
marker.pendown()

marker.right(180)
marker.forward(100)
marker.left(180)
marker.forward(100)
marker.right(90)

for side in range(3):
    marker.forward(50)
    marker.right(90)

marker.right(90)

for side in range(4):
    marker.forward(60)
    marker.right(90)







win.mainloop()