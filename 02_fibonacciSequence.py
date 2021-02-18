"""
Schrijf een programma dat een Fibonacci reeks opstelt. Als input verwacht het programma een getal dat aangeeft hoeveel elementen de reeks bevat.
Fibonacci getallen worden op de volgende manier opgesteld:
$$ f_{1} = 1 $$
$$ f_{2} = 1 $$
$$ f_{n} = f_{n-1} + f_{n-2} $$

Voorbeeld van de reeks met 8 cijfers:
1 1 2 3 5 8 13 21
"""

# Ask input from user
lengte_Fibonacci_reeks = int(input("Geef lengte van Fibonacci reeks: "))

# Fibonacci series
number_n_min_2 = 1
number_n_min_1 = 1
print(number_n_min_2)
print(number_n_min_1)

for i in range(lengte_Fibonacci_reeks - 2):
    number_n = number_n_min_1 + number_n_min_2
    number_n_min_2 = number_n_min_1
    number_n_min_1 = number_n
    print(number_n)

