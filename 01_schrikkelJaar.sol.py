"""
Schrijf een programma dat voor een gegeven getal bepaalt of het een schrikkeljaar is of niet.
Om een schrikkeljaar te zijn, moet voldaan zijn aan de volgende voorwaarden:
- het getal is deelbaar door 4
- het getal is niet deelbaar door 100 (!tenzij het deelbaar is door 400!)
Ter illustratie enkele voorbeelden van:
- een schrikkeljaar:  1600, 2000, 2004, 2008, 2012 en 2016
- geen schrikkeljaar:  1700, 1800, 2001, 2002, 2003
"""

year = int(input("Geef een getal in: "))

if year % 4 != 0:
    print("Dit is geen schrikkeljaar!")
elif year % 100 == 0 and year % 400 != 0:
    print("Dit is geen schrikkeljaar!")
else:
    print("Dit is een schrikkeljaar!")

# Merk op: de eerste twee statements kunnen nog samen genomen worden tot:
# if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#   print("Dit is geen schrikkeljaar!")



'''
Mijn oplossing
def schrikkeljaar(year):
    schrikkeljaar_boolean = False

    if year % 400 == 0:
        schrikkeljaar_boolean = True
    elif year % 4 == 0 and year % 100 != 0:
        schrikkeljaar_boolean = True

    return schrikkeljaar_boolean

year = int(input("Give a number: "))
if schrikkeljaar(year):
    print("Dit is een schrikkeljaar!")
else:
    print("Dit is geen schrikkeljaar.")'''