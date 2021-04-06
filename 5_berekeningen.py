"""
5.1 Faculteit
Schrijf een recursieve functie faculteit(n) die de faculteit 
van een gegeven parameter n berekent. Je mag ervan uitgaan 
dat n een natuurlijk getal is. Vermijd het gebruik van lussen.

"""
def faculteit(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n*faculteit(n-1)
    return result
assert faculteit(0) == 1
assert faculteit(1) == 1
assert faculteit(2) == 2
assert faculteit(6) == 720
assert faculteit(9) == 362880
"""
5.2 Machten
Schrijf een recursieve functie macht die x^n berekent.  
Je mag ervan uitgaan dat n een natuurlijk getal is. Denk 
goed na over de base case en controleer of de functie ook 
werkt voor n = 0. Vermijd het gebruik van lussen.

"""
def macht(grondtal, exponent):
    if grondtal == 0 and exponent == 0:
        result = "not defined"
    elif exponent == 0:
        result = 1
    elif grondtal == 0:
        result = 0
    else:
        result = grondtal*(macht(grondtal, exponent-1))
    return result

assert macht(0, 0) == 'not defined'
assert macht(0, 6) == 0
assert macht(6, 0) == 1
assert macht(3, 5) == 243
assert macht(6, 12) == 2176782336
assert macht(2, 0) == 1

"""
5.3  Priem ontbinding
Schrijf een recursieve functie die de ontbinding in priemfactoren 
van een positief geheel getal berekent. Bijvoorbeeld, voor n = 12, moet 
de functie [2, 2, 3] teruggeven. Vermijd het gebruik van lussen.
"""
from math import sqrt, floor
def factoren(getal):
    if getal == 1:
        result = []
    elif getal =
    elif getal % 2 == 0:
        result += [2]
        getal /= 2
    elif sqrt(getal) % 1 == 0:
        result += [sqrt(getal)]
        getal /= sqrt(getal)
    result += factoren(floor(sqrt(getal)))
    return result

print(factoren(49))
#print(factoren(1))
#print(factoren(7))
#print(factoren(9699690))



assert factoren(49) == [7, 7]
assert factoren(1) == []
assert factoren(7) == [3, 3, 3]
assert factoren(9699690) == [2, 3, 5, 7, 11, 13, 17, 19]

'''
    import math
number = int(input("Geef een getal in: "))

max_divisor_to_check = math.floor(math.sqrt(number))
divisor = 2
divisor_found = False

# Check deling door 2
# Merk op: alle even getallen > 2 moeten niet meer getest worden!
if number % divisor == 0:
    divisor_found = True
else:
    divisor += 1

while divisor <= max_divisor_to_check and not divisor_found:
    if number % divisor == 0:
        divisor_found = True
    else:
        divisor += 2

if divisor_found:
    print("Dit getal is geen priemgetal! (o.a.", divisor, "is een deler)")
else:
    print("Dit getal is een priemgetal!")
'''