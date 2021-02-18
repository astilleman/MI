"""
Schrijf een programma dat alle substrings van een gegeven woord print weergeeft gesorteerd volgens lengte.
(Extra: Probeer op voorhand te redeneren over de grootte orde van de output.)
"""

# Ask input from user
word = input("Geef een woord in: ")

# Substrings
for i in range(len(word)):
    for j in range(len(word) - i):
        print(word[j:j+i+1])
        j += 1
    i += 1


