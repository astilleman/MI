"""
Jump Search is een alternatieve manier om een element te zoeken
in een gesorteerde lijst. Gegeven sprong grootte m en gezocht
element x, het algoritme zal de elementen op index 0, m, 2*m, ...
vergelijken met x tot dat een interval is gevonden zodat
lijst[(i-1)*m] < x < lijst[i*m]. Uiteindelijk zal het algoritme
x lineair zoeken in dit interval. Schrijf een functie die Jump
Search gebruikt om de index van een element te zoeken in een lijst.
Zorg dat het algoritme als sprong grootte \verb|m| de vierkantswortel
van de lengte van de gegeven lijst gebruikt.
"""

def jump_search(x, lijst):
    pass


# Tests om te kijken of de implementatie correct is
assert jump_search(8, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 4
assert jump_search(5, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 2
assert jump_search(17, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 8
assert jump_search(12, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == -1
assert jump_search(18, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 9