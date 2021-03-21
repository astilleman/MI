"""
Schrijf met behulp van een while lus een programma dat het n-de fibonacci getal berekent.
Bewijs de correctheid.
"""
#VERIFIED fibonacci functie:
def fib(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a

n = int(input("Geef een getal: "))

f0 = 1
f1 = 1
i = 1

while i<n:
    temp = f0+f1
    f0 = f1
    f1 = temp
    i+=1

print("Het n-de fibonaccigetal is " + str(f0))
