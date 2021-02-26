# Constants (in inches)
DIAMETER = 12
CHORD_LENGTH = 10

# Calculation
# Gebruikte eigenschap: middellijn loodrecht op een koorde deelt de koorde middendoor

from math import sqrt

radius = DIAMETER / 2
half_chord_length = CHORD_LENGTH / 2
radius_minus_height = sqrt(radius ** 2 - half_chord_length ** 2)
height = radius - radius_minus_height
area = 2/3 * CHORD_LENGTH * height + (height ** 3)/(2 * CHORD_LENGTH)

# Print result
print("Area:", area)
