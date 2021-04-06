"""
Schrijf een recursieve functie die de grootste gemeenschappelijke 
deler berekent van twee gehele getallen a en b.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


# TESTS
assert gcd(2, 6)   == 2
assert gcd(24, 32) == 8
assert gcd(45, 55) == 5
assert gcd(13, 29) == 1
