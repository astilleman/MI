"""
Een n x n matrix is een magisch vierkant als de som van de elementen in elke rij, elke kolom en in de twee diagonalen
hetzelfde is.
Schrijf een programma dat gegeven een input van 16 getallen berekent of het over een magisch vierkant gaat.

Je mag de lijst hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.

Tip: gebruik aparte for lussen om na te kijken of alle kolommen, rijen en diagonalen tot hetzelfde getal sommeren.

Voorbeelden van magische vierkanten:
[[2, 16, 13, 3], [11, 5, 8, 10], [7, 9, 12, 6], [14, 4, 1, 15]]
[[8, 1, 6], [3, 5, 7], [4, 9, 2]]

Voorbeelden van niet magische vierkanten:
[[2, 13, 16, 3], [11, 8, 15, 10], [6, 9, 1, 7], [14, 4, 12, 5]]
[[3, 5, 4], [1, 9, 8], [2, 6, 7]]
"""
vierkant = [[2, 16, 13, 3], [11, 5, 8, 10], [7, 9, 12, 6], [14, 4, 1, 15]]

magisch_vierkant = True

som = 0
for i in range(len(vierkant)):
    som += vierkant[i][i]

#Itereer over de rijen
for rij in range(len(vierkant)):
    #Itereer over de kolommen
    rij_som = 0
    for kolom in range(len(vierkant[0])):
        rij_som += vierkant[rij][kolom]
    if rij_som != som:
        magisch_vierkant = False

#Itereer over de rijen
for kolom in range(len(vierkant[0])):
    #Itereer over de kolommen
    kolom_som = 0
    for rij in range(len(vierkant)):
        kolom_som += vierkant[rij][kolom]
    if kolom_som != som:
        magisch_vierkant = False

diagonaal_som = 0
#Itereer over de rijen
for i in range(len(vierkant)):
    #Itereer over de kolommen
    diagonaal_som += vierkant[i][len(vierkant) - 1 - i]
if diagonaal_som != som:
    magisch_vierkant = False

if magisch_vierkant:
    print("De gegeven matrix is een magisch vierkant")
else:
    print("De gegeven matrix is geen magisch vierkant")
