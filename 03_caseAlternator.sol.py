"""
Schrijf een programma dat een string inleest van de gebruiker en alternerend een hoofdletter en een kleine letter weergeeft. \\
*Hint:* Je kunt hiervoor gebruik maken van de functie upper().
    (Merk op dat characters die niet voldoen aan de isalpha() voorwaarde genegeerd worden!)
"""
#sentence = input("Geef een zin in: ")
'''
for i in range(len(sentence)):  # Gebruik indices omdat je alle chars wilt printen, maar toch alterneren!
    if i % 2 == 0:
        print(sentence[i].upper(), end="")
    else:
        print(sentence[i], end="")
'''

# Andere mogelijke oplossing gebruik makende van lists
# Merk op: Strings zijn immutable, lijsten niet!

splitted = list(input("Geef een zin:"))
for i in range(0, len(splitted)):
    if i % 2 == 0:
        splitted[i] = splitted[i].upper()
result = "".join(splitted)
print(result)