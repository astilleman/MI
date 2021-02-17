"""
Write a program that converts cartesian coordinates (x,y) to polar coordinates (r,theta).

Example:
    Enter the x-coordinate: 2.5
    Enter the y-coordinate: 2.5
    The radius is: 3.5355339059327378
    Theta is: 45.0

Hint: you will need functions defined in the math module
"""
from math import sqrt, atan, degrees

# Ask input from user
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Calculate radius r and angle theta
r = sqrt(x ** 2 + y ** 2)
theta = degrees(atan(y/x))

# Print result
print("The radius is:", r)
print("Theta is:", theta)