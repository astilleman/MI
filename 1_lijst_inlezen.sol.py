"""
Schrijf een programma dat elementen inleest en ze aan een lijst toevoegt indien het getal er nog niet in staat.
Wanneer de lijst 10 elementen bevat, wordt die geprint en stopt het programma.
"""
lijst = []
while len(lijst) < 10:
    nummer = int(input("Geef het volgende getal: "))
    if nummer not in lijst:
        lijst.append(nummer)

print("De lijst is " + str(lijst))
