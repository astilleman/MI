"""
Schrijf met behulp van een while lus een programma dat het kleinst gemeenschappelijke veelvoud van twee getallen berekent.
Bewijs de correctheid.
"""
num_1 = int(input('Geef getal 1: '))
num_2 = int(input('Geef getal 2: '))

kgv = num_1 * num_2
i = 1

while (i < kgv):
    if (i % num_1 == 0 and i % num_2 == 0):
        kgv = i
    else:
        i += 1

