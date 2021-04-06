"""
Schrijf een programma dat voor twee lijsten aangeeft of ze dezelfde elementen bevatten.
Elementen die meerdere keren voorkomen moeten ook even vaak in beide lijsten voorkomen.

Je mag de lijsten hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.

Tip: je kan gebruik maken van de sort() functie om de lijsten te sorteren.
De sort() functie werkt enkel als al je elementen van hetzelfde datatype zijn!
"""
lijst1 = [4, 7, 2, 2, 2, 1]
lijst2 = [1, 2, 2, 4, 7, 2]

lijst1.sort()  # merk op! wordt direct aangepast en returnt niks!
lijst2.sort()
if lijst1 == lijst2:
    print("De lijsten bevatten dezelfde elementen.")
else:
    print("De lijsten bevatten verschillende elementen.")
print(lijst1, lijst2)