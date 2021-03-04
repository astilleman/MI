"""
Schrijf een programma dat voor twee lijsten aangeeft of ze dezelfde elementen bevatten. 
Elementen die meerdere keren voorkomen moeten ook even vaak in beide lijsten voorkomen.

Je mag de lijsten hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen. 

Tip: je kan gebruik maken van de sort() functie om de lijsten te sorteren.
"""

# input
lijst1 = [1, 3, 5, 5, "beer", "beertje", "konijn"]
lijst2 = [3, "beer", "konijn", 5, 1, "beertje", 5]
lijst3 = [1, 3, 5, "beer", "beertje", "konijn"]
same = False

# Checking if lijst1 == lijst2
if len(lijst1) != len(lijst2):
    print("De lijsten zijn niet identiek")
else:
    for element in lijst1:
        if element in lijst2:
            lijst2.remove(element)

    if len(lijst2) == 0:
        print("De lijsten zijn identiek")

    else:
        print("De lijsten zijn niet identiek")
