'''taxrate = 5
taxrate = 5.5
taxrate = "joepie"
print(taxrate)
print(round(5.342))
print(round(5.342, 1))
from math import sqrt
a = 2
b = 3
c = 0.5
x1 = (-b + sqrt(b ** 2 - 4 * a * c)) \
    / (2 * a)
print(x1)
x2 = ((-b + sqrt(b ** 2 - 4 * a * c))
    / (2 * a))
print(x2)
greeting = "Hello"
print(greeting)
print('He said "Hello"')
print("C:\\\Temp\\Secret.txt")
love = 100
love2 = str(love)
print("%d%%" % love)
print( "%5d" % love)
pricePerOunce = 2.3590
print("Price per ounce: %8.2f" % pricePerOunce)'''

'''from ezgraphics import GraphicsWindow
win = GraphicsWindow(300,300)
canvas = win.canvas()

canvas.setColor("green")
canvas.drawRect(5, 4, 100, 200)

win.wait()
from ezgraphics import GraphicsWindow
window = GraphicsWindow (400, 200)
canvas = window.canvas( )
canvas.setBackground("red")
window.wait ( )

# input
richter = float(input("Give a number on the scale of richter: "))

# Conditions
if richter >= 8.0: # handle the special case first
    print("Most sructures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many builidngs damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed building")
else: # so that the 'general case' can be handled last
    print("No construction of building")

for i in range(0, 10, 2):
    print (i)

floor = int(input("Floor: "))
actual_floor = floor
if floor > 13:
    actual_floor -= 1
print("Actual floor: ", actual_floor)
print("Actural floor:", floor - 1 if floor > 13 else floor)


from sys import exit

userResponse = input("Enter n or y: ")
var = True

while var:
    if not(userResponse == "n" or userResponse == "y"):
        exit("Error: you must enter either n or y.")
    userResponse = input("Enter n or y: ")

'''
from ezgraphics import GraphicsWindow
from sys import exit
win = GraphicsWindow()
canvas = win.canvas()
x = int(input("Please enter the x-coordinate: "))
y = int(input("Please enter the y-coordinate: "))
if x < 0 or y < 0:
    exit("Error: x and y must be >= 0.")
canvas.drawOval(x - 5, y - 5, 10, 10)
point = win.getMouse()
x = point[0]
y = point[1]
canvas.drawRectangle(x, y, 40, 50)
win.wait()