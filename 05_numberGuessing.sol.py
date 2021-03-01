"""
Schrijf een programma dat een nummer raadt. Concreet genereert je programma een waarde tussen 0 en 20 waarna het de gebruiker vraagt om te gokken tot de juiste waarde gevonden is.
Implementeer verder ook "tips": geef mee aan de gebruiker van je programma of de ingegeven waarde hoger of lager ligt dan het gegenereerde getal.
Zorg er bovendien voor dat de gebruiker het programma kan stoppen wanneer hij -1 ingeeft!

Hint: maak gebruik van de (ingebouwde) random module om willekeurige getallen te genereren.

"""
import random

number = random.randint(0, 20)  # 0 en 20 behoren tot het interval!
guessed_number = int(input("Raad het getal (of -1 om te stoppen): "))

while guessed_number != number and guessed_number != -1:
    if guessed_number < number:
        print("Het getal is groter dan je gok!")
    else:
        print("Het getal is kleiner dan je gok!")
    guessed_number = int(input("Raad het getal (of -1 om te stoppen): "))

if guessed_number == - 1:
    print("Je koos om te stoppen, het programma is gestopt!")
else:
    print("Goed geraden, het nummer was inderdaad", number, "!")