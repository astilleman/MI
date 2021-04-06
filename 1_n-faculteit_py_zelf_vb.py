"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
import math
n = int(input('Geef een getal: '))
assert 0 <= n #PRECONDITIE
assert 1 <= 1 <= n + 1 and 1 == math.factorial(0)
# Als n >= 0 dan is dit equivalent met n + 1 >= 1 want we verhogen beide leiden gewoon met 1 en
# dan geldt zeker ook dat n>=1 en 0! = 1 dus OK!
fac = 1
assert 1 <= 1 <= n + 1 and fac == math.factorial(0)
i = 1
assert 1 <= i <= n + 1 and fac == math.factorial(i-1) #LUSINVARIANT
while (i < n + 1):
    oude_variant = n + 1 - i #LUSVARIANT
    assert 1 <= i <= n + 1 and fac == math.factorial(i - 1) and i < n + 1 and n + 1 - i == oude_variant
    assert 1 <= i + 1 <= n + 1 and fac*i == math.factorial(i) and 0 <= n + 1 - (i + 1) < oude_variant
    # Uit 1 <= i <= n + 1 en i < n + 1 volgt dat als i eentje verhoogt wordt ofwel kleiner, maar nu misschien ook gelijk kan zijn aan n + 1
    # dus 1 <= i + 1 <= n + 1 en n! = n*(n-1)! wegens de definitie van faculteit dus dit bepaalt de overgang van fac == math.factorial(i - 1)
    # naar fac*i == math.factorial(i) and als n + 1 - i == oude_variant dan is n + 1 -(i+1) of dus n + 1 - i - 1 < oude_variant dus OK!
    fac *= i
    assert 1 <= i + 1 <= n + 1 and fac == math.factorial(i) and 0 <= n+1 - (i+1) < oude_variant
    i += 1
    assert 1 <= i <= n + 1 and fac == math.factorial(i - 1) and 0 <= n+1 - i < oude_variant
assert 1 <= i <= n + 1 and fac == math.factorial(i-1) and not i < n + 1
assert fac == math.factorial(n) #POSTCONDITIE
# Uit 1 <= i <= n + 1 and not i < n + 1 volgt dat i == n + 1 end dit invullen in fac == math.factorial(i-1) geeft
# fac == math.factorial(n), wat de postconditie is dus OK!