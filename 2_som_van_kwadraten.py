"""
Schrijf met behulp van een while lus een programma dat de som van de kwadraten van 1 t.e.m. n berekent.
Bewijs de correctheid.
"""

# Helpfunctie (om de code te kunnen compilen).

def correcte_kwadraten_som_functie(n) :
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input('Geef een getal: '))

assert n > 0 # preconditie P (stap 1).
assert n + 1 >= 1 > 0  and 0 == correcte_kwadraten_som_functie(n) # OK, want uit n > 0 volgt dat n + 1 > 1 en dus ook n + 1 >= 1 en 1 > 0 is Z (eigenschap gehele getallen)
kwadraten_som = 0
assert n + 1 >= 1 > 0  and kwadraten_som == correcte_kwadraten_som_functie(n)
i = 1
assert n + 1 >= i > 0  and kwadraten_som == correcte_kwadraten_som_functie(n)
while i <= n:
    assert n + 1 >= i > 0 and kwadraten_som == correcte_kwadraten_som_functie(n) and i <= n
    assert n + 1 >= i + 1 > 0 and kwadraten_som + i**2 == correcte_kwadraten_som_functie(n) # OK, want uit n + 1 >= i > 0 en n >= i volgt dat n + 1 >= i + 1 > 0 en uit
    # correcte_kwadraten_som_functie(n) volgt wegens definitie som van kwadraten dat kwadraten_som + i**2 == correcte_kwadraten_som_functie(n)
    kwadraten_som += i**2
    assert n + 1 >= i + 1 > 0 and kwadraten_som == correcte_kwadraten_som_functie(n)
    i += 1
    assert n + 1 >= i > 0 and kwadraten_som == correcte_kwadraten_som_functie(n)
assert n + 1 >= i > 0  and kwadraten_som == correcte_kwadraten_som_functie(n) and not i <= n
assert kwadraten_som == correcte_kwadraten_som_functie(n) #  postconditie Q (stap 1). # OK want i == n+1 en dus kwadraten_som = correcte_kwadraten_som_functie(n) (stap 3).
# zelf not n >= i => n < i en n + 1 >= i => n >= i-1 ==> n == i - 1 ==> i = n + 1