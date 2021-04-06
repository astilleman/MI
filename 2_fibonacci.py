"""
Schrijf een functie die het n-de getal van de Fibonacci-reeks 
berekent. De Fibonacci-reeks is 1, 1, 2, 3, 5, 8, 13, 21, ... 
met het k-de getal gelijk aan de som van het (k-1)-de en het 
(k-2)-de getal.

Onderaan de file staan enkele 'assert' statements.
Wanneer je deze file runt, zullen die ook uitgevoerd worden 
en weet je of jeimplementatie al dan niet correct is.
"""



# TESTS
def fibonacci(n):
    if n == 1 or n==2:
        fibgetal = 1
    else:
        fibgetal = fibonacci(n-1) + fibonacci(n-2)
    return fibgetal
assert fibonacci(5) == 5
assert fibonacci(12) == 144
assert fibonacci(37)== 24157817
assert fibonacci(2) == 1
