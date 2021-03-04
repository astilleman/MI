"""
Een n x n matrix is een magisch vierkant als de som van de elementen in elke rij, elke kolom en in de twee diagonalen
hetzelfde is.13,
Schrijf een programma dat gegeven een input van 16 getallen berekent of het over een magisch vierkant gaat.

Je mag de lijst hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.

Tip: gebruik aparte for lussen om na te kijken of alle kolommen, rijen en diagonalen tot hetzelfde getal sommeren.

"""
#############OPTION1
'''
# Ask input from user

# Input
lijst = [2, 16, 13, 3, 11, 5, 8, 10, 7, 9, 12, 6, 14, 4, 1, 15]

# Kolommen
kolom_sommen = []
for i in range(4):
    kolom_som = lijst[0+4*i] + lijst[1+4*i] + lijst[2+4*i] + lijst[3+4*i]
    kolom_sommen.append(kolom_som)
    kolom_som = 0

# Rijen
rij_sommen = []
for i in range(4):
    rij_som = lijst[0 + i] + lijst[4 + i] + lijst[8 + i] + lijst[12 + i]
    rij_sommen.append(rij_som)
    rij_som = 0

# Diagonalen
hoofddiagonaal_som = lijst[0] + lijst[5] + lijst[10] + lijst[15]
nevendiagonaal_som = lijst[3] + lijst[6] + lijst[9] + lijst[12]

# Somlijst
somlijst = []
for element in kolom_sommen:
    somlijst.append(element)
for element in rij_sommen:
    somlijst.append(element)
somlijst.append(hoofddiagonaal_som)
somlijst.append(nevendiagonaal_som)

# 1 som of meerdere sommen
i = 1
som = somlijst[0]
zelfde_som = True
while zelfde_som and i < len(somlijst):
    if somlijst[i] != som:
        zelfde_som = False
    i += 1

# Print result
if i == len(somlijst):
    print("Dit is een magisch vierkant")
else:
    print("Dit is geen magisch vierkant")
'''
################OPTION2
# input
vierkant = [[11, 18, 25, 2, 9]
            ,[10, 12, 19, 21, 3]
            ,[4, 6, 13, 20, 22]
            ,[23, 5, 7, 14, 16]
            ,[17, 24, 1, 8, 15]]

# magisch vierkant?
magisch_vierkant = True

# hooddiagonaalsom
som = 0
for row in range(len(vierkant)):
    som += vierkant[row][row]

# rijsom == hoofddiagonaalsom?
for row in range(len(vierkant)):
    rijsom = 0
    for column in range(len(vierkant)):
        rijsom += vierkant[row][column]
    if rijsom != som:
        magisch_vierkant = False

# kolomsom == hoofddiagonaalsom?
for column in range(len(vierkant)):
    kolomsom = 0
    for row in range(len(vierkant)):
        kolomsom += vierkant[row][column]
    if kolomsom != som:
        magisch_vierkant = False

# nevendiagonaalsom == hoofddiagonaalsom?
nevendiagonaalsom = 0
for row in range(len(vierkant)):
    nevendiagonaalsom += vierkant[row][len(vierkant) - 1 - row]
if nevendiagonaalsom != som:
    magisch_vierkant = False

# Print result
if magisch_vierkant:
    print("Dit is een magisch vierkant met som", som)
else:
    print("Dit is geen magisch vierkant :(")