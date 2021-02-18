"""
Schrijf een programma dat een nummer raadt. Concreet genereert je programma een waarde tussen 0 en 20 waarna het de gebruiker vraagt om te gokken tot de juiste waarde gevonden is.
Implementeer verder ook "tips": geef mee aan de gebruiker van je programma of de ingegeven waarde hoger of lager ligt dan het gegenereerde getal.
Zorg er bovendien voor dat de gebruiker het programma kan stoppen wanneer hij -1 ingeeft!

Hint: maak gebruik van de (ingebouwde) random module om willekeurige getallen te genereren.

"""
from random import randint
# Generate random number
number_to_guess = randint(0, 20)

# initialisation
correct_number = False

# Ask input from user
guess = int(input("Raad het getal (of -1 om te stoppen): "))
while guess != -1 and not correct_number:
    if guess == number_to_guess:
        correct_number = True
        print("Goed geraden, het nummer was inderdaad", number_to_guess)
    elif number_to_guess > guess:
        print("Het getal is groter dan je gok!")
        guess = int(input("Raad het getal (of -1 om te stoppen): "))
    else:
        print("Het getal is kleiner dan je gok!")
        guess = int(input("Raad het getal (of -1 om te stoppen): "))




