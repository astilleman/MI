"""
Schrijf met behulp van een while lus een programma dat alle dubbele voorkomens uit een lijst verwijdert.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.
"""

# Helpfunctie (om code te compilen).
def correcte_verwijder_dubbels_functie(lijst):
    return list(dict.fromkeys(lijst))


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
# - P = 1 < len(lijst)
# - Q = lijst == correcte_verwijder_dubbels_functie(lijst)
# - I = 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i])
# - V = len(lijst) - i (wordt kleiner en blijft >= 0)
# - E = i < len(lijst)
# - E1 = lijst[i] in lijst[:i]

lijst = ["Troye", "Hayley", "Daya", "Trixie", "Years", "Years", "Daya", 2, 5, 2]

assert 1 < len(lijst) # 1. P

assert 0 <= 1 < len(lijst) and lijst[:1] == correcte_verwijder_dubbels_functie(lijst[:1]) # 2. propageer naar boven # 3. OK want uit len(lijst) > 1 volgt dat len(lijst) > 0; en lijst[0] == correcte_verwijder_dubbels_functie(lijst[0])
i = 1

assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) # 1. I
while i < len(lijst):
    oude_variant = len(lijst) - i # 1. oude_variant = V
    assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant # 1. assert I and E and V == oude_variant
    if lijst[i] in lijst[:i]:
        assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) \
               and i < len(lijst) and len(lijst) - i == oude_variant and lijst[i] in lijst[:i]  # 2. P' and E1
        assert 0 <= i <= (len(lijst)-1) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) \
               and 0 <= (len(lijst)-1) - i < oude_variant  # 2. propageer naar boven # 3. OK want ... (bewijs ieder conjunct op basis van vorige lijn)
        del lijst[i]
        assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) and 0 <= len(lijst) - i < oude_variant  # 2. propageer naar boven
    else:
        assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) \
               and i < len(lijst) and len(lijst) - i == oude_variant and not lijst[i] in lijst[:i]  # 2. P' and not E1
        assert 0 <= i+1 <= len(lijst) and lijst[:i+1] == correcte_verwijder_dubbels_functie(lijst[:i+1]) \
               and 0 <= len(lijst) - (i+1) < oude_variant # 2. propageer naar boven # 3. OK want ... (bewijs ieder conjunct op basis van vorige lijn)
        i += 1
        assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) \
               and 0 <= len(lijst) - i < oude_variant  # 2. propageer naar boven
    assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) and 0 <= len(lijst) - i < oude_variant # 1. assert I and 0 <= V < oude_variant
assert 0 <= i <= len(lijst) and lijst[:i] == correcte_verwijder_dubbels_functie(lijst[:i]) and not i < len(lijst) # 1. assert I and not E
assert lijst == correcte_verwijder_dubbels_functie(lijst) # 1. Q # 3. OK want i == len(lijst) en lijst[:len(lijst)] == lijst

print(lijst)