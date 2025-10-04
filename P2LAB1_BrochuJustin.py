# Justin Brochu
# 10/3/25
# P2LAB1
# Circle

import math

radius = float(input("What is the radius of the circle?"))
pi = math.pi
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2 
print("The diameter of the circle is", diameter)
print("The circumference of the circle is", "", end="")
print(f"{circumference:.2f}")
print("The area of the circle is","", end="")
print(f"{area:.3f}")