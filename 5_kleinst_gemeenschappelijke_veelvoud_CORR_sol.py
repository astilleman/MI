"""
Schrijf met behulp van een while lus een programma dat het kleinst gemeenschappelijke veelvoud van twee getallen berekent.
Bewijs de correctheid.
"""
import math

num_1 = int(input('Geef getal 1: '))
num_2 = int(input('Geef getal 2: '))
assert 0 < num_1 and 0 < num_2
assert 1 <= 1 <= num_1*num_2 and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,1))
# Indien num_1 > 0 en num_2 > 0, dan is het kleinste element waaraan num_1 en num_2 kunnen gelijk
# zijn beide 1. num_1*num_2 is dus minimaal 1 wat overeenkomt met de tweede assert statement.
# range(1,1) bevat geen elementen waardoor de tweede expressie in de tweede assert triviaal waar sinds
# de for-loop 0 iteraties doet.
kgv = num_1 * num_2
assert 1 <= 1 <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,1))
i = 1
assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i)) #voor alle natuurlijke getallen j waarvoor 0 < j < i, is j geen gemeenschappelijk veelvoud van num_1 en num_2
while (i < kgv):
    oude_variant = kgv-i #dit verkleint elke iteratie
    assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and i < kgv and kgv-i == oude_variant
    if i % num_1 == 0 and i % num_2 == 0:
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and kgv-i == oude_variant and i % num_1 == 0 and i % num_2 == 0
        assert 1 <= i <= i and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and 0 <= i-i < oude_variant
        # Aangezien i%num_1 == 0 en i%nym_2 == 0 is dit een veelvoud van num_1 en num_2.
        # De tweedd conditie in beiden asserts komen overeen met elkaar en dus moet hier niet verder over
        # geredeneerd worden.
        kgv = i
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i)) and 0 <= kgv-i < oude_variant
    else:
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1, i)) and kgv-i == oude_variant and not (i % num_1 == 0 and i % num_2 == 0)
        assert 1 <= i+1 <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i+1)) and 0 <= kgv-(i+1) < oude_variant
        # Omdat minstens een van (num_1,num_2) geen deler is van i, betekent dit dat i geen gemeenschappelijk veelvoud is van num_1 en num_2.
        # Omdat de eerste i-1 elementen ook geen deler zijn (uit de eerste assert) volgt hieruit dat in de tweede assert geldt dat alle elementen in de range [1,i+1[ ook
        # niet deelbaar is door zowel num_1 als num_2. Hierdoor is de tweede expressie in de tweede assert een logisch gevolg van de eerste assert.
        i += 1
        assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i)) and 0 <= kgv-i < oude_variant
    assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i)) and 0 <= kgv-i < oude_variant

assert 1 <= i <= kgv and all(not (j % num_1 == 0 and j % num_2 == 0) for j in range(1,i)) and not i < kgv
assert kgv == math.lcm(num_1,num_2)
# Indien i == kgv en elk element kleiner dan i niet gedeeld wordt door zowel num_1 als num_2 moet het wel gelden
# i of dus kgv het kleinste gemeenschappelijke veelvoud is. Dit komt omdat de variabele kgv steeds aangepast wordt
# enkel indien beide getallen delers zijn van het getal in kgv.
print("Het kleinst gemeenschappelijke veelvoud van " + str(num_1) + " en " + str(num_2) + " is " + str(kgv))