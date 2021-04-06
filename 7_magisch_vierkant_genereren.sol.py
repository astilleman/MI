"""
Schrijf een programma dat een magisch vierkant van grootte n x n construeert.
Je kan hiervoor volgende algoritme implementeren:

Set row = n - 1, column = n // 2
For k = 1..n*n
    Place k at [row][column]
    Increment row and column
    If row or column is n, replace it with 0
    If the element at [row][column] has already been filled
        Set row and column to their previous values
        Decrement row

Merk op: dit algoritme werkt enkel wanneer n oneven is!

Een voorbeeld uitvoer van je programma zou als volgt kunnen zijn:

Geef de grootte van het magisch vierkant: 5
Het magisch vierkant is
[11, 18, 25, 2, 9]
[10, 12, 19, 21, 3]
[4, 6, 13, 20, 22]
[23, 5, 7, 14, 16]
[17, 24, 1, 8, 15]
"""
n = int(input("Geef de grootte van het magisch vierkant: "))

matrix = [[0 for i in range(n)] for j in range(n)]

rij = n - 1
kolom = n // 2

for k in range(1, n*n+1):
    matrix[rij][kolom] = k

    vorige_rij = rij
    rij += 1

    vorige_kolom = kolom
    kolom += 1

    if rij == n:
        rij = 0
    if kolom == n:
        kolom = 0
    if matrix[rij][kolom] != 0:
        rij = vorige_rij
        kolom = vorige_kolom
        rij -= 1

print("Het magisch vierkant is")
for i in range(len(matrix)):
    print(matrix[i])
