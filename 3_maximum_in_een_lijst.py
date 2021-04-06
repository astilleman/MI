"""
Schrijf met behulp van een while lus een programma dat het grootste element in een lijst van getallen berekent.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.

Extra:Wat gebeurt er als er zowel integers als strings in je lijst kunnen zitten?
Hoe zou je je preconditie uitbreiden om dit probleem te voorkomen?
"""

# TOTALE CORRECTHEID

# Te bewijzen:
# assert P
# while E:
#   assert P' # P' volgt uit de condities in de lus boven P'.
#   if E1: # E1 is verschillend van E.
#         p1
#   else:
#         p2
#   assert Q' # Q' volgt uit de condities in de lus onder Q'.
# assert Q

# Bewijs:
# assert P
# assert I # OK
# while E:
#   oude_variant = V
#   assert I and E and V == oude_variant
#   assert P' (P' is gelijk aan de vorige lijn)
#   if E1:
#       assert P' and E1
#       p1
#       assert Q'
#   else:
#       assert P' and not E1
#       p2
#       assert Q'
#   assert Q' (Q' is gelijk aan de volgende lijn)
#   assert I and 0 <= V < oude_variant
# assert I and not E
# assert Q # OK

# We kiezen:
# - P = 1 <= len(lijst)
# - Q = max_ == max(lijst)
# - I = 1 <= i <= len(lijst) and max_ == max(lijst[:i])
# - V = len(lijst) - i (wordt kleiner en blijft >= 0)
# - E = i < len(lijst)
# - E1 = lijst[i] > max_

lijst = [1,2,3,4,5]

assert 1 <= len(lijst) # 1. P

assert 1 <= 1 <= len(lijst) and lijst[0] == max(lijst[:1]) # 2. naar boven propageren # 3. OK want bevat zelfde conditie (i.e., 1 <= len(lijst)) en max(lijst[0]) == lijst[0].
i = 1
assert 1 <= i <= len(lijst) and lijst[0] == max(lijst[:i]) # 2. naar boven propageren
max_ = lijst[0] # We voegen _ toe omdat de naam "max" al gebruikt wordt voor een built-in functie.

assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) # 1. I
while i < len(lijst):
    oude_variant = len(lijst) - i # 1. oude_variant = V
    assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant # 1. I and E and V == oude_variant
    if lijst[i] > max_:
        assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and lijst[i] > max_ # 1. I and E and V == oude_variant and E1
        assert 1 <= i+1 <= len(lijst) and lijst[i] == max(lijst[:i+1]) and 0 <= len(lijst) - (i+1) < oude_variant # 2. naar boven propageren # 3. OK
        max_ = lijst[i]
        assert 1 <= i+1 <= len(lijst) and max_ == max(lijst[:i+1]) and 0 <= len(lijst) - (i+1) < oude_variant # 2. naar boven propageren
    else:
        assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and not lijst[i] > max_ # 1. I and E and V == oude_variant and not E1
        assert 1 <= i+1 <= len(lijst) and max_ == max(lijst[:i+1]) and 0 <= len(lijst) - (i+1) < oude_variant # 2. naar boven propageren # 3. OK
        pass
        assert 1 <= i+1 <= len(lijst) and max_ == max(lijst[:i+1]) and 0 <= len(lijst) - (i+1) < oude_variant # 2. naar boven propageren
    assert 1 <= i+1 <= len(lijst) and max_ == max(lijst[:i+1]) and 0 <= len(lijst) - (i+1) < oude_variant # 2. naar boven propageren
    i += 1
    assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) and 0 <= len(lijst) - i < oude_variant # 1. I and 0 <= V < oude_variant

assert 1 <= i <= len(lijst) and max_ == max(lijst[:i]) and not i < len(lijst) # 1. I and not E
assert max_ == max(lijst) # 1. Q # 3. OK want i == len(lijst) en dus max_ == max(lijst[:len(lijst)] == max(lijst)

#ZELF
'''
Uit te breiden preconditie
and getal_boolean_funtie(lijst)
Dit op voorhand definiëren in functie
def getal_boolean_functie(lijst):
    getal_boolean = True
    for getal in lijst:
        if not str(getal).isdigit():
            getal_boolean = False
    return getal_boolean

assert getal_boolean_functie([1, 2, 44, 23]) == True
assert getal_boolean_functie([1, 2, "44", 23]) == True
assert getal_boolean_functie([1, 2, "koe", 23]) == False
'''