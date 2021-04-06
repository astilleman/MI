"""
Schrijf een recursieve functie die de grootste gemeenschappelijke 
deler berekent van twee gehele getallen a en b.
"""
def gcd(getal1, getal2):
    if getal1 % getal2 == 0:
        return getal2
    else:
        return gcd(getal2, getal1 % getal2)

# TESTS
assert gcd(2, 6)   == 2
assert gcd(24, 32) == 8
assert gcd(45, 55) == 5
assert gcd(13, 29) == 1

