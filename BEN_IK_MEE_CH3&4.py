'''
Schrijf een programma dat
Een aantal getallen inleest (sentinel -1)
En nadien
uitschrijft of er een even getal werd ingegeven
uitschrijft hoeveel van die getallen deelbaar zijn door 3


Snel opgelost? Breid uit met input-validatie
Gebruiker geeft mogelijks tekst in die geen getal voorstelt…
'''

# initialisation
even_number = False
count_multiples_of_3 = 0
number = -1

# Read the first value with validation input
inputStr = input("Enter a positive number or -1 to finish: ")
if inputStr != "":
    number = float(inputStr)

# We will keep on processing values until a negative value is input or number is even
while number >= 0:
    if number % 2 == 0:
        even_number = True
    if number % 3 == 0:
        count_multiples_of_3 += 1
    inputStr = input("Enter a positive number or -1 to finish: ")
    if inputStr != "":
        number = float(inputStr)
    else:
        number = -1

# print
if even_number is True:
    print("Er werd een even nummer ingegeven.")
else:
    print("Er werden enkel oneven nummers ingegeven.")
print("Er werden", count_multiples_of_3, "getallen die deelbaar zijn door 3 ingegeven.")
