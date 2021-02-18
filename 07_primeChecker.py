"""
Schrijf een programma dat checkt of het ingegeven getal een priemgetal is of niet.
Als het getal geen priemgetal heeft, geef dan ook een van delers weer!
Probeer te denken aan de efficiëntie van je programma!
    (*Hint:* Tot en met welke deler moet je testen? Is er een verschil tussen even en oneven delers?)
"""

from math import sqrt, floor

# Initialisation
i = 2

# Ask input from user
number = int(input("Geef een getal in: "))

# Checking whether number is prime
while i <= floor(sqrt(number)) and number % i != 0:
    i += 1
if i == floor(sqrt(number)) + 1:
    print("Dit getal is een priemgetal!")
else:
    print("Dit getal is geen priemgetal! (o.a.", i, "is een deler)")


