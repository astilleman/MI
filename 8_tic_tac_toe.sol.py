"""
Schrijf een programma dat tic-tac-toe speelt.

Tic-tac-toe is een spel dat op een 3 x 3 raster gespeeld wordt. Het spel wordt gespeeld door twee spelers, die elk
om beurt spelen. De eerste speler markeert zijn zetten met een cirkel, de tweede met een kruisje.
De eerste speler die er in slaagt om een horizontale, verticale of diagonale rij van zijn symbooltjes te maken wint.

Je programma moet het spelbord tekenen en aan de gebruiker de coordinaten vragen voor zijn volgende zet.

De (0,0) coördinaat van het spelbord bevindt zich in de linkerbovenhoek.

Een mogelijke uitvoer van je programma kan als volgt zijn:

['.', '.', '.']
['.', '.', '.']
['.', '.', '.']
Speler 1 is aan zet!
Geef x coördinaat in: 1
Geef y coördinaat in: 1
['.', '.', '.']
['.', 'O', '.']
['.', '.', '.']
Speler 2 is aan zet!
Geef x coördinaat in: 0
Geef y coördinaat in: 0
['X', '.', '.']
['.', 'O', '.']
['.', '.', '.']
Speler 1 is aan zet!
Geef x coördinaat in: 1
Geef y coördinaat in: 0
['X', 'O', '.']
['.', 'O', '.']
['.', '.', '.']
Speler 2 is aan zet!
Geef x coördinaat in: 1
Geef y coördinaat in: 2
['X', 'O', '.']
['.', 'O', '.']
['.', 'X', '.']
Speler 1 is aan zet!
Geef x coördinaat in: 0
Geef y coördinaat in: 2
['X', 'O', '.']
['.', 'O', '.']
['O', 'X', '.']
Speler 2 is aan zet!
Geef x coördinaat in: 2
Geef y coördinaat in: 0
['X', 'O', 'X']
['.', 'O', '.']
['O', 'X', '.']
Speler 1 is aan zet!
Geef x coördinaat in: 0
Geef y coördinaat in: 1
['X', 'O', 'X']
['O', 'O', '.']
['O', 'X', '.']
Speler 2 is aan zet!
Geef x coördinaat in: 2
Geef y coördinaat in: 2
['X', 'O', 'X']
['O', 'O', '.']
['O', 'X', 'X']
Speler 1 is aan zet!
Geef x coördinaat in: 2
Geef y coördinaat in: 1
['X', 'O', 'X']
['O', 'O', 'O']
['O', 'X', 'X']
Speler 1 heeft gewonnen!
"""

spelbord = [["." for i in range(3)] for j in range(3)]
for i in range(len(spelbord)):
    print(spelbord[i])


speler = 0
gewonnen = False

while not gewonnen:

    if speler == 0:
        teken = "O"
    else:
        teken = "X"
    print("Speler " + str(speler+1) + " is aan zet!")
    x = int(input("Geef x coördinaat in: "))
    y = int(input("Geef y coördinaat in: "))
    spelbord[y][x] = teken

    # Kijk na of de eerste diagonaal gevormd is
    if spelbord[0][0] == teken and spelbord[1][1] == teken and spelbord[2][2] == teken:
        gewonnen = True

    # Kijk na of de tweede diagonaal gevormd is
    if spelbord[0][2] == teken and spelbord[1][1] == teken and spelbord[2][0] == teken:
        gewonnen = True

    # Kijk na of er een rij gevormd is
    for i in range(len(spelbord)):
        if spelbord[i][0] == teken and spelbord[i][1] == teken and spelbord[i][2] == teken:
                gewonnen = True

    # Kijk na of er een kolom gevormd is
    for i in range(len(spelbord)):
        if spelbord[0][i] == teken and spelbord[1][i] == teken and spelbord[2][i] == teken:
                gewonnen = True

    for i in range(len(spelbord)):
        print(spelbord[i])
    if not gewonnen:
        speler = (speler + 1) % 2

print("Speler " + str(speler + 1) + " heeft gewonnen!")