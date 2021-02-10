##
# This program calculates the zero-points of a 2nd degree equation
#

from math import sqrt

# Obtain coefficients of a 2nd degree equation
a = float(input("Enter the coefficient of the 2nd degree term: "))
b = float(input("Enter the coefficient of the 1st degree term: "))
c= float(input("Enter the coefficient of the consant term: " ))

# Calculate discriminant (we may assume that discriminant >= 0)
# 2 cases: 1 zero-point or 2 zero-points
discriminant = b ** 2 - 4 * a * c
if discriminant == 0:
    zero_point = (-b + sqrt(discriminant)) / (2 * a)
    result = "Het enige nulpunt is " + str(zero_point)
else:
    zero_point1 = (-b + sqrt(discriminant)) / (2 * a)
    zero_point2 = (-b - sqrt(discriminant)) / (2 * a)
    result = "De nulpunten zijn " + str(zero_point1) + " en " + str(zero_point2)

# Print result
print(result)


