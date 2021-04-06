"""
Schrijf een programma dat een sequentie inputs leest en dan de input waarden als een bar chart weergeeft zoals in
volgend voorbeeld:

    ****************************
    ****************************************
    *********************************
    *************************
    **********
Je mag er van uitgaan dat alle ingegeven waarden positieve getallen zijn.
Zoek eerst de maximale waarde en ken hier 40 sterren aan toe, de andere bars hebben proportioneel minder sterren.

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
MAXIMAL_BAR_LENGTH = 40

n = int(input("Geef de volgende waarde in (-1 om te stoppen): "))

lijst = []
while n != -1:
    lijst.append(n)
    n = int(input("Geef de volgende waarde in (-1 om te stoppen): "))

maximum = max(lijst)

print("Bar chart")
for i in range(len(lijst)):
    print("*" * ((lijst[i] * MAXIMAL_BAR_LENGTH) // maximum))
