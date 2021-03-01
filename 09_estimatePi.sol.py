"""
Schrijf een getal dat pi benaderend berekent. Dit kan op volgende manier:
- Genereer random waardes in [-1,1] voor de x- en y-coördinaten.
- Controleer of de ingegeven coördinaten behoren tot de cirkel met straal 1 en middelpunt (0,0).
- Gebruik de verhouding in_circle/NUMBER_OF_TRIALS en de formule voor de oppervlakte van een cirkel om pi te berekenen.

Hint: maak gebruik van de (ingebouwde) random module om willekeurige getallen te genereren.
Merk op: Hoe meer herhalingen van dit kansspel, hoe nauwkeuriger de benaderde waarde van pi wordt.

################ Uitleg: ########################
oppervlakte cirkel: pi * r**2 = pi * 1**2 = pi
oppervlakte vierkant: zijde**2 = 2**2 = 4
"random punt" (ligt in vierkant!): (x,y) = (random[-1,1],random[-1,1])

Kans dat "random punt" in de cirkel ligt = (oppervlakte cirkel) / (oppervlakte vierkant) = pi / 4
==> als je een "random punt" neemt (zie hierboven), is er 79% kans dat het in de cirkel ligt

Voor VEEL punten geldt dus het volgende:
(aantal punten in de cirkel) / (totaal aantal punten) = pi / 4
= 79% procent van de punten liggen binnen de cirkel
--> pi = (aantal punten in de cirkel) / (totaal aantal punten) * 4

Merk op: hoe meer punten gebruikt worden hoe nauwkeuriger de benadering is over het algemeen!
"""
import random
import math

AMOUNT_OF_POINTS = 10000  # Note: experimenteer met deze waarde!
points_in_circle = 0

for i in range(AMOUNT_OF_POINTS):
    x_coord = random.uniform(-1, 1)
    y_coord = random.uniform(-1, 1)
    #  gebruik stelling van pythagoras: als de lengte van de schuine zijde <= 1 --> ligt in de cirkel
    if math.sqrt(x_coord**2 + y_coord**2) <= 1:
        points_in_circle += 1
print("De benadering van pi: " + str((points_in_circle / AMOUNT_OF_POINTS) * 4))

