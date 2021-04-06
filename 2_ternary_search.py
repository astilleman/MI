"""
Binary Search zoekt door een gesorteerde lijst in twee te splitsen en
vervolgens in slechts één helft verder te zoeken. Het Ternary Search
algoritme werkt analoog, maar zal de gesorteerde lijst in drie gelijke
delen splitsen. Implementeer een zoek algoritme om de index van een
gegeven waarde in een gesorteerde lijst te zoeken, gebruik makende van
het Ternary Search algoritme. Indien het element niet in de lijst
voorkomt, dan moet het algoritme -1 terug geven.
"""
# x staat voor target, lijst voor values
def ternary_search(x, lijst):
    return ternary_search_with_low_and_hight(x, lijst, len(lijst)//2, len(lijst))

def ternary_search_with_low_and_hight(x, lijst, one, two, three):
    if one <= two:
        third = (low+high)//3

        if lijst[third] == x:
            return third
        elif lijst[third] < x:
            return ternary_search_with_low_and_hight(x, lijst, third+1, high)
        else:
            return ternary_search_with_low_and_hight(x, lijst, low, third-1)
    else:
        return -1








# Tests om te kijken of de implementatie correct is
assert ternary_search(8, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 4
assert ternary_search(5, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 2
assert ternary_search(17, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 8
assert ternary_search(12, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == -1