from math import sqrt

"""
Dit programma zal
aan de gebruiker de coëfficienten vragen van een 2e-graads-functie, en
de nulpunten van deze functie berekenen en uitschrijven

    f(x) = a.x^2 + b.x + c

Je mag ervan uitgaan dat de functie 1 of 2 nulpunten zal hebben, dus dat de coëfficiënten zo zullen zijn dat de discriminant niet negatief is

Algoritme
    vraag getallenaan de gebruiker
        a, b, c
    bereken discriminant = b**2 - 4ac
    bereken nulpunt 1 = (-b + sqrt(discriminant)) / (2a)
    bereken nulpunt 2 = (-b - sqrt(discriminant)) / (2a)
"""

# vraag invoer aan gebruiker
a = float (input("Geef waarde voor coefficient a: "))
b = float (input("Geef waarde voor coefficient b: "))
c = float (input("Geef waarde voor coefficient c: "))

# bereken de discrimiant
discriminant = b*b - 4*a*c

# bereken nulpunten
nulpunt1 = (- b + sqrt(discriminant)) / (2*a)
nulpunt2 = (- b - sqrt(discriminant)) / (2*a)

# schrijf resultaat uit
print ("De nulpunten van deze veelterm zijn:")
print ("  eerste nulpunt: ", nulpunt1)
print ("  tweede nulpunt: ", nulpunt2)
