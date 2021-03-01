"""
Schrijf een programma dat alle substrings van een gegeven woord print weergeeft gesorteerd volgens lengte.
(Extra: Probeer op voorhand te redeneren over de grootte orde van de output.)
"""
word = input("Geef een woord in: ")

for substr_len in range(1, len(word) + 1):
    for start_pos in range(len(word) - substr_len + 1):
        print(word[start_pos: start_pos + substr_len])