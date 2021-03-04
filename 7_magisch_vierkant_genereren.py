"""
Schrijf een programma dat een magisch vierkant van grootte n x n construeert.
Je kan hiervoor volgende algoritme implementeren:

Set row = n - 1, column = n // 2
For k = 1..n*n
    Place k at [row][column]
    Increment row and column
    If the row or column is n, replace it with 0
    If the element at [row][column] has already been filled
        Set row and column to their previous values
        Decrement row

Een voorbeeld uitvoer van je programma zou als volgt kunnen zijn:

Geef de grootte van het magisch vierkant: 5
Het magisch vierkant is
[11, 18, 25, 2, 9]
[10, 12, 19, 21, 3]
[4, 6, 13, 20, 22]
[23, 5, 7, 14, 16]
[17, 24, 1, 8, 15]
"""
'''
from random import randint
# Ask input from user
n = int(input("Geef de grootte van het magisch vierkant: "))

# Initialisatie
magisch_vierkant = []

# Constructie magisch vierkant
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(0, 100))
    magisch_vierkant.append(row)

print(magisch_vierkant)
'''

# Ask input from user
n = int(input("Geef de grootte van het magisch vierkant: "))

# Initialisation
magisch_vierkant = [[0 for row in range(n)] for column in range(n)]

# Calculation
row = n - 1
column = n // 2
for k in range(1, n*n + 1):
    magisch_vierkant[row][column] = k
    previous_row = row
    previous_column = column
    row += 1
    column += 1
    if row == n:
        row = 0
    if column == n:
        column = 0
    if magisch_vierkant[row][column] != 0:
        row = previous_row
        column = previous_column
        row -= 1

# Print result
print("Het magisch vierkant is")
for row in magisch_vierkant:
    print(row)


