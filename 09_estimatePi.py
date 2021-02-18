"""
Schrijf een getal dat pi benaderend berekent. Dit kan op volgende manier:
- Genereer random waardes in [-1,1] voor de x- en y-coördinaten.
- Controleer of de ingegeven coördinaten behoren tot de cirkel met straal 1 en middelpunt (0,0).
- Gebruik de verhouding in_circle/NUMBER_OF_TRIALS en de formule voor de oppervlakte van een cirkel om pi te berekenen.

Hint: maak gebruik van de (ingebouwde) random module om willekeurige getallen te genereren.
Merk op: Hoe meer herhalingen van dit kansspel, hoe nauwkeuriger de benaderde waarde van pi wordt.
"""
from random import random


'''
# Generating random numbers - Dit is niet methode die ze willen (boek)
from random import uniform
x = uniform(-1, 1)
y = uniform(-1, 1)'''

# Initialisation
hits = 0
TRIES = 1000000

# For-loop
for i in range(TRIES):

    # Generate 2 random numbers between -1 and 1
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2*r

    # Check whether the point lies in the unit circle
    if x * x + y * y <= 1:
        hits = hits + 1

# The ratio hits/tries is approximately the same as the ratio
# circle area / square area = pi / 4
piEstimate = 4.0 * hits / TRIES

# Print result
print("De schatting van pi is:", piEstimate)





