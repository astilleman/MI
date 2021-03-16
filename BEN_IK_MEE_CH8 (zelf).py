"""
Schrijf een programma dat een lijst van wegverbindingen gegeven krijgt. Bv.:

Leuven:Brussel
Brussel:Antwerpen
Antwerpen:Hasselt
Antwerpen:Gent
Gent:Brussel

(Je mag dit inlezen uit een bestand of van de toetsenbord-invoer of gewoon als een lijst van strings (of een lijst van paren van strings, dus een lijst van lijsten of tuples) in het programma definiëren.)

Het moet als uitvoer voor elke stad de steden geven die met die stad een wegverbinding hebben:

Antwerpen: Brussel Gent Hasselt
Brussel: Antwerpen Gent Leuven
Gent: Antwerpen Brussel
Hasselt: Antwerpen
Leuven: Brussel

Zowel de gehele lijst als de lijst per stad moeten in alfabetische volgorde gegeven worden.
"""

# Input data
wegverbindingen = []
steden = set()
wegdictionary = {}
weglijst = []
wegenstring = ""
weg = input("Geef stad:stad: ")
while weg != "Q":
    wegverbindingen.append(weg)
    weg = input("Geef stad:stad: ")

for element in wegverbindingen:
    paar = element.split(":")
    for stad in paar:
        steden.add(stad)
        weglijst.append(stad)

for stadje in sorted(steden):
    wegdictionary[stadje] = set()

for i in range(len(weglijst)):
    if i % 2 == 0:
        wegdictionary[weglijst[i]].add(weglijst[i+1])
    else:
        wegdictionary[weglijst[i]].add(weglijst[i-1])

for wegenuitleg in wegdictionary.items():
    wegenopsomming = sorted(wegenuitleg[1])
    for stad in wegenopsomming:
        wegenstring += stad + " "
    print(wegenuitleg[0] + ": " + wegenstring)
    wegenstring = ""


#print(wegdictionary)






#print(steden)
#print(wegverbindingen)