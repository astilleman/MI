"""
Schrijf een programma dat voor een gegeven getal bepaalt of het een schrikkeljaar is of niet.
Om een schrikkeljaar te zijn, moet voldaan zijn aan de volgende voorwaarden:
- het getal is deelbaar door 4
- het getal is niet deelbaar door 100 (!tenzij het deelbaar is door 400!)
Ter illustratie enkele voorbeelden van:
- een schrikkeljaar:  1600, 2000, 2004, 2008, 2012 en 2016
- geen schrikkeljaar:  1700, 1800, 2001, 2002, 2003
"""

# Ask input from user
number = int(input("Geef een getal in: "))

# schrikkeljaar?
if (number % 4 == 0 and number % 100 != 0) or number % 400 == 0:
    print("Dit is een schrikkeljaar!")
else:
    print("Dit is geen schrikkeljaar!")


