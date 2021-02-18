"""
Schrijf een programma dat de grootste gemeenschappelijke deler van twee getallen (=input) berekent.
Hint: je kunt hiervoor gebruik maken van het Algoritme van Euclides.
"""
'''
from math import gcd

# Ask input from user
getal1 = int(input("Geef het getal 1: ")
getal2 = int(input("Geef het getal 2: ")

# Calculation gcd
grootste_gemeenschappelijke_deler = gcd(getal1, getal2)

# Print result
print("De grootste gemeenschappelijke deler is", grootste_gemeenschappelijke_deler)
'''

# Algoritme van Euclides

#from math import max

# Ask input from user
getal1 = int(input("Geef het getal 1: "))
getal2 = int(input("Geef het getal 2: "))

# THE algorithm
largest_number = max(getal1, getal2)
smallest_number = min(getal1, getal2)
rest = largest_number % smallest_number

while rest != 0:
    largest_number = smallest_number
    smallest_number = rest
    rest = largest_number % smallest_number

# Print result
print("De grootste gemeenschappelijke deler is", smallest_number)
