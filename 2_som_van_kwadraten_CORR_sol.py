"""
Schrijf met behulp van een while lus een programma dat de som van de kwadraten van 1 t.e.m. n berekent.
Bewijs de correctheid.
"""

n = int(input('Geef een getal: '))

assert 0 <= n
assert  1 <= 1 <= n+1 and 0 == sum(x**2 for x in range(1))
# Als je in 0 <= n beide leden met 1 verhoogt krijg je 1 <= n+1
# Het tweede deel is waar want sum([0^2])=0^2=0
som = 0
assert 1 <= 1 <= n+1 and som == sum(x**2 for x in range(1))
i = 1
assert 1 <= i <= n+1 and som == sum(x**2 for x in range(i))
while (i < n + 1):
    oude_variant = n+1-i
    assert 1 <= i <= n+1 and som == sum(x**2 for x in range(i)) and i < n+1 and n+1-i == oude_variant
    assert  1 <= i+1 <= n+1 and som + i**2 == sum(x**2 for x in range(i+1)) and 0 <= n+1-(i+1) < oude_variant
    # OK want als 1 <= i <= n+1 en i < n+1 waar zijn, dan geldt i <= i < n+1.
    # Dus i < n+1, i+1 is dan oftewel ook kleiner maar mogelijks ook gelijk aan n+1 
    # en dus volgt hieruit dat 1 <= i+1 <= n+1 geldt in de tweede assert. 
    # De tweede statement in beide asserts zijn consistent want range(v) loopt tot en met v-1 dus 
    # als je dan de berekening uitbreidt met het volgende element (v dus), dan bekom
    # je de kwadratische som van de lijst met 1 element extra.
    som += i**2
    assert  1 <= i+1 <= n+1 and som == sum(x**2 for x in range(i+1)) and 0 <= n+1-(i+1) < oude_variant
    i += 1
    assert 1 <= i <= n+1 and som == sum(x**2 for x in range(i)) and 0 <= n+1-i < oude_variant
assert 1 <= i <= n+1 and som == sum(x**2 for x in range(i)) and not i < n+1
assert som == sum(x**2 for x in range(n+1))
# OK want i == n+1 (wegens de eerste en derde uitdrukking in de eerste assert) invullen in
# som == sum(x**2 for x in range(i)) geeft som == sum(x**2 for x in range(n+1)) wat de
# postconditie (tweede assert) is
print("De som van de kwadraten van 1 t.e.m. n is " + str(som))