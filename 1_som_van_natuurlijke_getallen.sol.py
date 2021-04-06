"""
Schrijf een functie die de som van alle natuurlijke getallen tot 
en met een gegeven getal berekent: som(n) = 1 + 2 + ... + n

Onderaan de file staan enkele 'assert' statements.
Wanneer je deze file runt, zullen die ook uitgevoerd worden 
en weet je of je implementatie al dan niet correct is.
"""

def som(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

# TESTS
assert som(1) == 1
assert som(5) == 15
assert som(100) == 5050

