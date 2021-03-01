"""
Schrijf een programma dat de grootste gemeenschappelijke deler van twee positieve gehele getallen (=input) berekent.
Hint: je kunt hiervoor gebruik maken van het Algoritme van Euclides.
"""
a = int(input("Geef het getal 1: "))
b = int(input("Geef het getal 2: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("De grootste gemeenschappelijke deler is", a)