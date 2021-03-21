"""
Schrijf met behulp van een while lus een programma dat het grootste element in een lijst van getallen berekent.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.

Extra:Wat gebeurt er als er zowel integers als strings in je lijst kunnen zitten?
Hoe zou je je preconditie uitbreiden om dit probleem te voorkomen?
"""
lijst = [34.2,7,9,2,-5,1.98,23,-42,28.7,-1,-19,34.3, -3.10]
max = lijst[0]
i = 1

while i<len(lijst):
    if lijst[i] > max:
        max = lijst[i]
	i+=1

print(max)
