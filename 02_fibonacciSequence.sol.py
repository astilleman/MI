"""
Schrijf een programma dat een Fibonacci reeks opstelt. Als input verwacht het programma een postief getal dat aangeeft hoeveel elementen de reeks bevat.
Fibonacci getallen worden op de volgende manier opgesteld:
$$ f_{1} = 1 $$
$$ f_{2} = 1 $$
$$ f_{n} = f_{n-1} + f_{n-2} $$

Voorbeeld van de reeks met 8 cijfers:
1 1 2 3 5 8 13 21
"""
sequence_length = int(input("Geef lengte van Fibonacci reeks: "))

a = 0
b = 1

for i in range(sequence_length):
    print(b)
    c = a  # een tijdelijke variabele!
    a = b
    b = c + b

# Merk op: Python ondersteunt ook onderstaande (kortere notatie)!
# a, b = b, a + b
