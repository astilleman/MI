"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
import math
n = int(input('Geef een getal: '))

fac = 1
i = 1

while (i < n + 1):
    fac *= i
    i += 1
