##
#  Compute the section of a hull at position x.
#

# Gather input from the user.
b = float(input("Enter B: "))
l = float(input("Enter L: "))
t = float(input("Enter T: "))
x = float(input("Enter x: "))
n = int(input("Enter n: "))

# Initialize z, total_area and prev_y.
z = 0
total_area = 0
prev_y = (b / 2) * (1 - ((2 * x) / l) ** 2) * (1 - ((z / t) ** 2))

# Step from 0 up to but not including -t by z / t, computing the area for
# each trapezoid and adding it to the total area.
while z > -t :
   z = z - t / n
   y = (b / 2) * (1 - ((2 * x) / l) ** 2) * (1 - ((z / t) ** 2))
   # Opp trapezium = ((B+b)*h)/2 met B = prev_y, b = y, h = z/t
   total_area = total_area + -0.5 * (y + prev_y) * (z / t)
   prev_y = y

# Display the total area.
print("The total area is", total_area)