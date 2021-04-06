"""
Schrijf met behulp van een while lus een programma dat het kleinst gemeenschappelijke veelvoud van twee getallen berekent.
Bewijs de correctheid.
"""
import math
num_1 = int(input('Geef getal 1: '))
num_2 = int(input('Geef getal 2: '))
assert 0 <= num_1 and 0 <= num_2
assert 1 <= 1 <= num_1*num_2 and all(not(j % num_1 == 0 and j % num_2 == 0) for j in range(1, 1))
kgv = num_1 * num_2
assert 1 <= 1 <= kgv and all(not(j % num_1 == 0 and j % num_2 == 0) for j in range(1, 1))
i = 1
assert 1 <= i <= kgv and all(not(j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) #LUSINVARIANT
while (i < kgv):
    oude_variant = kgv - i
    assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and i < kgv and kgv - i == oude_variant
    if (i % num_1 == 0 and i % num_2 == 0):
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and i< kgv and kgv - i == oude_variant and \
           i % num_1 == 0 and i % num_2 == 0
        assert 1 <= i <= i and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and 0 <= i - i < oude_variant
    #
        kgv = i
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and 0 <= kgv - i < oude_variant
    else:
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and i < kgv and kgv - i == oude_variant and \
            not( i % num_1 == 0 and i % num_2 == 0)
        assert 1 <= i+1 <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i+1)) and 0 <= kgv - (i+1) < oude_variant
        i += 1
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and 0 <= kgv - i < oude_variant
    assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and 0 <= kgv - i < oude_variant
assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and not i < kgv
assert kgv == math.lcm(num_1, num_2) #POSTCONDITIE
# Uit 1 <= i <= kgv en not i < kgv volgt dat i == kgv en dit leidt samen met all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i))
# tot kgv == math.lcm(num_1, num_2), wat de postconditie is dus OK!