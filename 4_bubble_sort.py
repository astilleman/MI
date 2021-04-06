"""
Bubble Sort is een sorteer algoritme dat aangrenzende waarden
in een lijst vergelijkt, en indien nodig wisselt van plaats.
Schrijf een functie die het Bubble Sort algoritme gebruikt om
een lijst te sorteren.
"""

def bubble_sort(lijst):
    if len(lijst) == 0:
        return
    elif len(lijst) == 1:
        return lijst
    else:
        if lijst[0] < lijst[1]:
            lijst[0] ,lijst[1] = lijst[1], lijst[0]
    return lijst[:1] + bubble_sort(lijst[1:])


lijst = [20, 18, 10, 6, 15, 3, 9, 7, 11, 20, 9, 5, 12, 8, 17]
bubble_sort(lijst)
print("Gesorteerde lijst: ", lijst)