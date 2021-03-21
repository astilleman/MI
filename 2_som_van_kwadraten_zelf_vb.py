"""
Schrijf met behulp van een while lus een programma dat de som van de kwadraten van 1 t.e.m. n berekent.
Bewijs de correctheid.
"""
n = int(input('Geef een getal: '))

som = 0
i = 1

while (i < n + 1):
    som += i**2
    i += 1

