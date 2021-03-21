"""
Een van de vereisten van het correctheidsbewijs is niet voldaan, welke? Pas het programma aan zodat het correct werkt.
Hint: Je moet maar 1 lijn in het programma aanpassen.

Dit programma berekent de som van alle oneven elementen van 1 t.e.m. 20.
"""
i = 1
som = 0
while i <= 20: #was while i!=20
    som += i
    i += 2
print(som)

#EINDIGHEID is niet voldaan
#Het programma komt in een oneindige lus
#Dit omdat i geinitialiseert wordt op 1 en telkens met 2 verhoogd wordt
#i zal dus altijd een oneven getal zijn, en zal van 19 naar 21 verhoogd worden
#het kan dus nooit dat i==20
#de conditie veranderen zorgt dat het programma wel eindigt