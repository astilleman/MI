"""
Schrijf een programma dat een sequentie inputs leest en dan de input waarden als een bar chart weergeeft zoals in
volgend voorbeeld:

    ****************************
    ****************************************
    *********************************
    *************************
    **********
Je mag er van uitgaan dat alle waarden positief zijn. Zoek eerst de maximale waarden en ken hier 40 sterren aan toe,
de andere bars hebben proportioneel minder sterren.

Een voorbeeld uitvoer van je programma kan als volgt zijn:

Geef de volgende waarde in (-1 om te stoppen): 50
Geef de volgende waarde in (-1 om te stoppen): 100
Geef de volgende waarde in (-1 om te stoppen): 10
Geef de volgende waarde in (-1 om te stoppen): 25
Geef de volgende waarde in (-1 om te stoppen): -1
Bar chart
********************
****************************************
****
**********
Tip: je kan ook hier gebruik maken van de max() functie.
"""
# Initialisation
numberlist = []

# Ask input from user
number = int(input("Geef de volgende waarde in (-1 om te stoppen): "))
if number != -1:
    numberlist.append(number)
    while number != -1:
        number = int(input("Geef de volgende waarde in (-1 om te stoppen): "))
        numberlist.append(number)
else:
    exit()

# Calculation and print result
maximum = max(numberlist)
print("Bar chart")
for number in numberlist:
    print('*'*(40*number//maximum))