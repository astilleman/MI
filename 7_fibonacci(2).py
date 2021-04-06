"""
Schrijf met behulp van een while lus een programma dat het n-de fibonacci getal berekent. In het bewijs zal dit geschreven worden als fib(n)
Bewijs de correctheid.
"""
#VERIFIED fibonacci functie:
def fib(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a


n = int(input("Geef een getal: "))
assert 0 < n
assert 1 <= 1 <= n and 1 == fib(1) and 1 == fib(2)
# Het is duidelijk dat als n>0 is, dan is n minstens 1 onder de aanname
# dat n een int is. De tweede en derde expressie in de tweede assert
# is eenvoudig na te kijken want de eerste 2 elementen van de Fibonacci
# reeks zijn 1 en 1.
f0 = 1
assert 1 <= 1 <= n and f0 == fib(1) and 1 == fib(2)
f1 = 1
assert 1 <= 1 <= n and f0 == fib(1) and f1 == fib(2)
i = 1
assert 1 <= i <= n and f0 == fib(i) and f1 == fib(i+1)
while i < n:
    oude_variant = n-i
    assert 1 <= i <= n and f0 == fib(i) and f1 == fib(i+1) and i < n and n-i == oude_variant
    assert 1 <= i + 1 <= n and f1 == fib(i + 1) and f0+f1 == fib(i + 2) and 0 <= n-(i+1) < oude_variant
    # OK want als 1 <= i <= n+1 en i < n+1 waar zijn, dan geldt i <= i < n+1.
    # Dus i < n+1, i+1 is dan oftewel ook kleiner maar mogelijks ook gelijk aan n+1 
    # en dus komt dit overeen met 1 <= i+1 <= n+1 in de tweede assert. 
    # Indien, f0 en f1 twee opeenvolgende fibonnaci getallen zijn, dan kunnen we
    # gebruik maken van de formule voor de Fibonacci reeks: f_i+2 = f_i+1 + f_i.
    # f0 en f1 hierin invullen geeft f2 = f1 + f0 = f_i+1 + f_i = f_i+2.
    temp = f0+f1
    assert 1 <= i + 1 <= n and f1 == fib(i + 1) and temp == fib(i + 2) and 0 <= n-(i+1) < oude_variant
    f0 = f1
    assert 1 <= i+1 <= n and f0 == fib(i+1) and temp == fib(i + 2) and 0 <= n-(i+1) < oude_variant
    f1 = temp
    assert 1 <= i+1 <= n and f0 == fib(i+1) and f1 == fib(i + 2) and 0 <= n-(i+1) < oude_variant
    i+=1
    assert 1 <= i <= n and f0 == fib(i) and f1 == fib(i + 1) and 0 <= n-i < oude_variant
assert 1 <= i <= n and f0 == fib(i) and f1 == fib(i+1) and not i < n
assert f0 == fib(n)
# Na substitutie van i==n in de expressie f0 = fib(i) bekomen we
# f0 = fib(n), wat de postconditie is

print("Het n-de fibonaccigetal is " + str(fib(n)))
