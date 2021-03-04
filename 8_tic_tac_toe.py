"""
Schrijf een programma dat tic-tac-toe speelt.

Tic-tac-toe is een spel dat op een 3 x 3 raster gespeeld wordt. Het spel wordt gespeeld door twee spelers, die elk
om beurt spelen. De eerste speler markeert zijn zetten met een cirkel, de tweede met een kruisje.
De eerste speler die er in slaagt om een horizontale, verticale of diagonale rij van zijn symbooltjes te maken wint.

Je programma moet het spel bord tekenen en aan de gebruiker de coordinaten vragen voor zijn volgende zet.

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
# Initialisation
matrix = [['.' for row in range(3)] for column in range(3)]
spel_afgelopen = False
speler = 1

# Wanneer spel afgelopen
def is_afgelopen(matrix):
    spel_afgelopen = False
    for row in range(1, 3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2] != '.':
            spel_afgelopen = True
    for column in range(1, 3):
        if matrix[0][column] == matrix[1][column] == matrix[2][column] != '.':
            spel_afgelopen = True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != '.':
        spel_afgelopen = True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != '.':
        spel_afgelopen = True
    return spel_afgelopen

# Game
for row in matrix:
    print(row)
print("Speler 1 is aan zet!")
x = int(input("Geef x coördinaat (0, 1, 2) in: "))
y = int(input("Geef x coördinaat (0, 1, 2) in: "))
matrix[y][x] = 'O'
for row in matrix:
    print(row)
while not is_afgelopen(matrix):
    print("Speler 2 is aan zet!")
    speler = 2
    x = int(input("Geef x coördinaat (0, 1, 2) in: "))
    y = int(input("Geef x coördinaat (0, 1, 2) in: "))
    matrix[y][x] = 'X'
    for row in matrix:
        print(row)
    print("Speler 1 is aan zet!")
    speler = 1
    x = int(input("Geef x coördinaat (0, 1, 2) in: "))
    y = int(input("Geef x coördinaat (0, 1, 2) in: "))
    matrix[y][x] = 'O'
    for row in matrix:
        print(row)

# Print result
print("Speler", speler, "heeft gewonnen!")

