"""
Schrijf een programma dat checkt of het ingegeven positieve getal een priemgetal is of niet.
Als het getal geen priemgetal heeft, geef dan ook een van delers weer!
Probeer te denken aan de efficiëntie van je programma!
    (*Hint:* Tot en met welke deler moet je testen? Is er een verschil tussen even en oneven delers?)
"""
import math
number = int(input("Geef een getal in: "))

max_divisor_to_check = math.floor(math.sqrt(number))
divisor = 2
divisor_found = False

# Check deling door 2
# Merk op: alle even getallen > 2 moeten niet meer getest worden!
if number % divisor == 0:
    divisor_found = True
else:
    divisor += 1

while divisor <= max_divisor_to_check and not divisor_found:
    if number % divisor == 0:
        divisor_found = True
    else:
        divisor += 2

if divisor_found:
    print("Dit getal is geen priemgetal! (o.a.", divisor, "is een deler)")
else:
    print("Dit getal is een priemgetal!")

