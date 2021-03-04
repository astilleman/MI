"""
Schrijf een programma dat getallen inleest en ze aan een lijst toevoegt indien het getal er nog niet in staat.
Wanneer de lijst 10 getallen bevat, wordt de lijst geprint en stopt het programma.
"""

# Initialisation
lijst = []

# Ask input from user
while len(lijst) < 10:
    element = input("Enter an element: ")
    if element not in lijst:
        lijst.append(element)

# Print result
print(lijst)