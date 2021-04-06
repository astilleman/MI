"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
# input
n = int(input("Geef een geheel getal: "))

# programma
assert 1 <= n
assert 1 <= 1 <= n + 1 and 1 == n_faculteit(0) # OK
i = 1
assert 1 <= i <= n + 1 and 1 == n_faculteit(i-1)
n_faculteit = 1
assert 1 <= i <= n + 1 and n_faculteit == n_faculteit(i-1)
while i <= n:
    assert 1 <= i <= n + 1 and n_faculteit == n_faculteit(i-1) and i <= n
    assert 1 <= i + 1 <= n + 1 and n_faculteit*i == n_faculteit(i)
    n_faculteit = n_faculteit * i
    assert 1 <= i + 1 <= n + 1 and n_faculteit == n_faculteit(i)
    i = i + 1
    assert 1 <= i <= n + 1 and n_faculteit == n_faculteit(i-1)
assert 1 <= i <= n + 1 and n_faculteit == n_faculteit(i-1) and not i <= n
assert n_faculteit == n_faculteit(n)

print(n_faculteit)

