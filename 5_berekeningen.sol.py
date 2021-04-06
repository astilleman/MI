"""
5.1 Faculteit
Schrijf een recursieve functie faculteit(n) die de faculteit 
van een gegeven parameter n berekent. Je mag ervan uitgaan 
dat n een natuurlijk getal is. Vermijd het gebruik van lussen.

"""

def faculteit(n):
    if n <= 0:
        return 1
    return n * faculteit(n-1)

n = int(input("Geef een nummer: "))
print("Faculteit van " + str(n) +  " is ", faculteit(n))


"""
5.2 Machten
Schrijf een recursieve functie macht die x^n berekent.  
Je mag ervan uitgaan dat n een natuurlijk getal is. Denk 
goed na over de base case en controleer of de functie ook 
werkt voor n = 0. Vermijd het gebruik van lussen.

"""

def macht(x,n):
    if n <= 0:
        return 1
    return x * macht(x,n-1)

x = int(input("Geef x: "))
n = int(input("Geef n: "))
print("De macht van " + str(x) + " tot " + str(n) + " is ", macht(x,n))

"""
5.3  Priem ontbinding
Schrijf een recursieve functie die de ontbinding in priemfactoren 
van een positief geheel getal berekent. Bijvoorbeeld, voor n = 12, moet 
de functie [2, 2, 3] teruggeven. Vermijd het gebruik van lussen.
"""

# Methode die een combinatie gebruikt van zowel iteraties als recursie
def factoren(x, deler = 2):
    if x == 1:
        return []
    for i in range(deler, int( x ** .5 ) + 1 ):
        if x % i == 0:
            return [i] + factoren(int(x / i), i)
    return [x]
    
# Methode die enkel recursie gebruikt
def factoren2(x, deler = 2):
    if x < deler:
        return []
    if x % deler == 0:
        return [deler] + factoren2(int(x / deler), 2)
    return factoren2(x, deler + 1)

n = int(input("Geef een nummer: "))
print("De factoren van " + str(n) + " zijn: ", factoren(n))
