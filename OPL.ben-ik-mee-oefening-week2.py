"""
Schrijf een programma dat
Een aantal getallen inleest (sentinel -1)
En nadien
uitschrijft of er een even getal werd ingegeven
uitschrijft hoeveel van die getallen deelbaar zijn door 3


Snel opgelost? Breid uit met input-validatie
Gebruiker geeft mogelijks tekst in die geen getal voorstelt…
"""

# initialisatie van variabelen
er_is_een_getal_dat_even_is = False
aantal_getallen_deelbaar_door_3 = 0


# vraag naar getal + input-validatie
tekst = input("Geef getal (geef -1 als alle invoer is ingegeven): ")
while not (tekst.isdigit() or tekst == "-1"):
    tekst = input("Geef een geldig getal (geef -1 als alle invoer is ingegeven): ")
getal = int(tekst)

# in de volgende while-lus worden 1 na 1 de ingegeven getallen verwerkt
while getal != -1:
    # we verwerken het laatst-ingelezen getal
    if getal % 2 == 0:
        er_is_een_getal_dat_even_is = True
    if getal % 3 == 0:
        aantal_getallen_deelbaar_door_3 += 1


    # vraag naar volgend getal + input-validatie
    tekst = input("Geef volgende getal (geef -1 als alle invoer is ingegeven): ")
    while not (tekst.isdigit() or tekst == "-1"):
        tekst = input("Geef een geldig getal (geef -1 als alle invoer is ingegeven): ")
    getal = int(tekst)

# uitschrijven van het resultaat
if er_is_een_getal_dat_even_is:
    print("Er was een even getal.")
else:
    print("Er waren geen even getallen.")

print("Het aantal getallen deelbaar door 3 is", aantal_getallen_deelbaar_door_3)

# ZELF uitbreiding naar negatieve getallen
'''
# initialisatie van variabelen
er_is_een_getal_dat_even_is = False
aantal_getallen_deelbaar_door_3 = 0

#input-validatie
def input_validatie():
    tekst = input("Geef getal (geef -1 als alle invoer is ingegeven): ")
    while not ((tekst[0] == "-" and tekst[1:].isdigit()) or tekst.isdigit() or tekst == "-1"):
        tekst = input("Geef een geldig getal (geef -1 als alle invoer is ingegeven): ")
    return int(tekst)


getal = input_validatie()

# in de volgende while-lus worden 1 na 1 de ingegeven getallen verwerkt
while getal != -1:
    # we verwerken het laatst-ingelezen getal
    if getal % 2 == 0:
        er_is_een_getal_dat_even_is = True
    if getal % 3 == 0:
        aantal_getallen_deelbaar_door_3 += 1


    # vraag naar volgend getal + input-validatie
    getal = input_validatie()

# uitschrijven van het resultaat
if er_is_een_getal_dat_even_is:
    print("Er was een even getal.")
else:
    print("Er waren geen even getallen.")

print("Het aantal getallen deelbaar door 3 is", aantal_getallen_deelbaar_door_3)'''