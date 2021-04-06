"""
Schrijf een programma dat gegeven twee lijsten deze in een lijst samenvoegt waarvan de elementen alterneren.
Dus als de eerste lijst
    [1, 4, 9, 16]
is en de tweede lijst
    [9, 7, 4, 9, 11]
dan wordt het resultaat
    [1, 9, 4, 7, 9, 4, 16, 9, 11]

Je mag de lijsten hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.

Tip: je kan gebruik maken van de max() functie om de lengte van de langste lijst te vinden.
"""
lijst1 = [1, 4, 9, 16]
lijst2 = [9, 7, 4, 9, 11]

lijst = []
for i in range(max(len(lijst1), len(lijst2))):
    if i < len(lijst1):
        lijst.append(lijst1[i])
    if i < len(lijst2):
        lijst.append(lijst2[i])


print("De samengevoegde lijst is: " + str(lijst))
