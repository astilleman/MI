"""
Schrijf een programma dat een positief geheel decimaal getal omzet naar binaire vorm.
"""

dec_number = int(input("Geef een positief geheel decimaal getal in: "))
remaining_dec_number = dec_number
bin_number = ""

if dec_number == 0:
    bin_number = "0"
else:
    while remaining_dec_number > 0:
        bin_number = str(remaining_dec_number % 2) + bin_number
        remaining_dec_number = remaining_dec_number // 2

print("De binaire representatie van", dec_number, " is:", bin_number)

# Merk op: Python heeft een ingebouwde (geoptimaliseerde) functie die dit doet: bin()
