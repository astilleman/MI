"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
import math

n = int(input('Geef een getal: '))

# PRE: n is een natuurlijk getal
assert 0<=n
assert  1<=1<=n+1 and 1 == math.factorial(0)
# Beide asserts ok want beide leden in 0 <= n verhogen met 1 levert 1<=n+1 op
# Het tweede deel van de tweede assert is triviaal aan voldaan.
i = 1
assert  1<=i<=n+1 and 1 == math.factorial(i-1)
fac = 1
assert 1<=i<=n+1 and fac == math.factorial(i-1) #LUSINVARIANT
while (i < n+1):
    oude_variant = n+1-i
    assert 1<=i<=n+1 and fac == math.factorial(i-1) and i<n+1 and n+1-i == oude_variant
    assert  1<=i+1<=n+1 and fac*i == math.factorial(i) and 0 <= n+1-(i+1) < oude_variant
    # Beide asserts ok want als je in assert1 je de eerste en laatste conditie
    # samenneemt bekom je 1 <= i < n+1. Indien i verhoogd wordt met 1 dan kan deze
    # nu wel mogelijks gelijk zijn aan n+1 wat verantwoordt dat we i+1 <= n+1 hebben
    # in de tweede assert. De tweede conditie in beide asserts zijn ook ok want als
    # fac effectief (i-1)! is, dan is (i-1)!*i = 1*2*...*(i-1)*i = i!.
    fac *= i
    assert 1<=i+1<=n+1 and fac == math.factorial(i) and 0 <= n+1-(i+1) < oude_variant
    i += 1
    assert 1<=i<=n+1 and fac == math.factorial(i-1) and 0 <= n+1-i < oude_variant

assert 1<=i<=n+1 and fac == math.factorial(i-1) and not i<n+1
assert fac == math.factorial(n)
# Beide asserts ok want als je de eerste en laatste conditie in de eerste assert
# samenneemt bekom je i == n+1 omdat de while loop conditie niet geldt. Dit
# subsitueren in [fac == math.factorial(i-1)] geeft [fac == math.factorial(n)]
# wat exact de postconditie is (de assert eronder).

print(str(n) + '! = ' + str(fac))