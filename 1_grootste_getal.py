"""
Schrijf een recursieve functie grootste_getal die
het grootste getal in een lijst zoekt.
"""

def grootste_getal(lijst):
    if len(lijst) == 0:
        return
    elif len(lijst) == 1:
        return lijst[0]
    elif lijst[0] < lijst[1]:
        del lijst[0]
    else:
        del lijst[1]
    return grootste_getal(lijst)


# Tests om te kijken of de implementatie correct is
assert grootste_getal([2, 15, 5, 16, 20, 9, 3, 15, 6]) == 20
assert grootste_getal([5, 11, 5, 14, 12, 2, 5, 14, 11]) == 14
assert grootste_getal([10, 7, 19, 12, 5, 3, 13, 9, 4]) == 19
assert grootste_getal([17, 5, 17, 5, 6, 2, 3, 16, 6]) == 17