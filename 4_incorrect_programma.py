"""
Een van de vereisten van het correctheidsbewijs is niet voldaan, welke? Pas het programma aan zodat het correct werkt.
Hint: Je moet maar 1 lijn in het programma aanpassen.

Dit programma berekent de som van alle oneven elementen van 1 t.e.m. 20.
"""

i = 1
som = 0
while i!=20:
    som += i
    i += 2
print(som)

# EINDIGHEID is niet voldaan.

# Het programma komt in een oneindige lus
# Dit komt omdat i geïnitialiseert wordt op 1 en telkens met 2 verhoogd wordt.
# i zal dus altijd een oneven getal zijn (en zal van 19 naar 21 verhoogd worden en dus nooit gelijk zijn 20).

# Als we V (de lusvariant) = som - i dan is V < 0 voor i == 21,
# en is dus aan de regel 0 <= V < oude_variant niet voldaan.

# Oplossing E = i != 21 of E = i <= 20 (in while E:).