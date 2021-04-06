"""
Schrijf een functie die het n-de getal van de Fibonacci-reeks 
berekent. De Fibonacci-reeks is 1, 1, 2, 3, 5, 8, 13, 21, ... 
met het k-de getal gelijk aan de som van het (k-1)-de en het 
(k-2)-de getal.

Onderaan de file staan enkele 'assert' statements.
Wanneer je deze file runt, zullen die ook uitgevoerd worden 
en weet je of jeimplementatie al dan niet correct is.
"""

def fibonacci(n):
    first = 1
    second = 1

    if n == 1:
        return first
    if n == 2:
        return second
    else:
        min_2 = first
        min_1 = second
        i = 3
        while i < n + 1:
            fib = min_2 + min_1
            min_2 = min_1
            min_1 = fib
            i += 1
        return fib


# TESTS
assert fibonacci(5) == 5
assert fibonacci(12) == 144
assert fibonacci(37) == 24157817
assert fibonacci(2) == 1
