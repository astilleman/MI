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
# Input
lijst1 = [1, 4, 9 , 16]
lijst2 = [9, 7, 4, 9, 11]

# Grootste en kleinste lijst
grootste_lijst = max(lijst1, lijst2)
kleinste_lijst = min(lijst1, lijst2)

# Initialisatie
lijst = []

# Samenvoegen
for i in range(len(kleinste_lijst)*2):
    if i % 2 == 0:
        lijst.append(lijst1[0])
        del lijst1[0]
    else:
        lijst.append(lijst2[0])
        del lijst2[0]
rest_grootste_lijst = grootste_lijst[len(kleinste_lijst):len(grootste_lijst)]
for element in rest_grootste_lijst:
    lijst.append(element)

# Print result
print(lijst)

