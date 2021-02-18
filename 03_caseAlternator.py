"""
Schrijf een programma dat een string inleest van de gebruiker en alternerend een hoofdletter en een kleine letter weergeeft. \\
*Hint:* Je kunt hiervoor gebruik maken van de functie upper().
    (Merk op dat characters die niet voldoen aan de isalpha() voorwaarde genegeerd worden!)
"""

# Ask input from user
string = input("Geef een zin: ")

# Initialisation
new_string = ""

# Changing in upper and lower case letters
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i].upper()
    else:
        new_string += string[i].lower()

# Print result
print(new_string)

