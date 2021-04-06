# Het programma hieronder telt het aantal keren dat de waarde 0 voorkomt
# in de gegeven lijst xs. Het plaatst het resultaat in variabele n.

i = 0
n = 0
while i < len(xs):
    if xs[i] == 0:
        n = n + 1
    else:
        pass
    i = i + 1

# Voorzie dit programma van een gepaste preconditie en postconditie en
# bewijs haar correctheid.

# Voorzie twee bewijzen: één waarbij je partiële correctheid bewijst,
# en één waarbij je totale correctheid bewijst.

# Opmerking bij modeloplossing: de vorm van verantwoordingen van gevolgtrekkingen
# is vrij. We passen hier, louter als voorbeeld, de vorm toe die beschreven wordt
# op https://github.com/btj/proofchecker .

# Partiële correctheid:

# Wet LeAntisym: a <= b <= a ==> a == b
# Wet LenNonnegative: 0 <= len(xs)
# Wet SliceFull: xs[:len(xs)] == xs
# Wet NbZerosEmpty: nb_zeros(xs[i:i]) == 0
# Wet NbZerosZero: 0 <= i and i < len(xs) and xs[i] == 0 ==> nb_zeros(xs[:i + 1]) == nb_zeros(xs[:i]) + 1
# Wet NbZerosNonzero: 0 <= i and i < len(xs) and xs[i] != 0 ==> nb_zeros(xs[:i + 1]) == nb_zeros(xs[:i])

assert True
assert 0 <= 0 <= len(xs) and 0 == nb_zeros(xs[:0]) # Z of LenNonnegative of NbZerosEmpty
i = 0
assert 0 <= i <= len(xs) and 0 == nb_zeros(xs[:i])
n = 0
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) # Lusinvariant
while i < len(xs):
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs)
    if xs[i] == 0:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and xs[i] == 0
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and nb_zeros(xs[:i]) + 1 == nb_zeros(xs[:i + 1]) # NbZerosZero op 1 en 4 en 5
        assert 0 <= i + 1 <= len(xs) and n + 1 == nb_zeros(xs[:i + 1]) # Z op 1 of Z op 2 of Herschrijven met 3 in 4
        n = n + 1
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    else:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and not xs[i] == 0
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and xs[i] != 0 # Z op 5
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and nb_zeros(xs[:i]) == nb_zeros(xs[:i + 1]) # NbZerosNonzero op 1 en 2 en 4
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) # Z op 1 of Z op 2 of Herschrijven met 3 in 4
        pass
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    i = i + 1
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i])
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and not i < len(xs)
assert len(xs) <= i <= len(xs) and n == nb_zeros(xs[:i]) # Z op 4
assert i == len(xs) and n == nb_zeros(xs[:i]) # LeAntisym op 1 en 2
assert n == nb_zeros(xs[:len(xs)]) # Herschrijven met 1 in 2
assert n == nb_zeros(xs) # Herschrijven met SliceFull in 1

# Totale correctheid:

# Wet LeAntisym: a <= b <= a ==> a == b
# Wet LenNonnegative: 0 <= len(xs)
# Wet SliceFull: xs[:len(xs)] == xs
# Wet NbZerosEmpty: nb_zeros(xs[i:i]) == 0
# Wet NbZerosZero: 0 <= i and i < len(xs) and xs[i] == 0 ==> nb_zeros(xs[:i + 1]) == nb_zeros(xs[:i]) + 1
# Wet NbZerosNonzero: 0 <= i and i < len(xs) and xs[i] != 0 ==> nb_zeros(xs[:i + 1]) == nb_zeros(xs[:i])

assert True
assert 0 <= 0 <= len(xs) and 0 == nb_zeros(xs[:0]) # Z of LenNonnegative of NbZerosEmpty
i = 0
assert 0 <= i <= len(xs) and 0 == nb_zeros(xs[:i])
n = 0
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) # Lusinvariant
while i < len(xs):
    oude_variant = len(xs) - i # Lusvariant
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant
    if xs[i] == 0:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant and xs[i] == 0
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and nb_zeros(xs[:i]) + 1 == nb_zeros(xs[:i + 1]) and len(xs) - i == oude_variant # NbZerosZero op 1 en 4 en 6
        assert 0 <= i + 1 <= len(xs) and n + 1 == nb_zeros(xs[:i + 1]) and len(xs) - i == oude_variant # Z op 1 of Z op 2 of Herschrijven met 3 in 4
        assert 0 <= i + 1 <= len(xs) and n + 1 == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant # Z op 2 of Z op 4
        n = n + 1
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant
    else:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant and not xs[i] == 0
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and xs[i] != 0 and len(xs) - i == oude_variant # Z op 6 
        assert 0 <= i < len(xs) and n == nb_zeros(xs[:i]) and nb_zeros(xs[:i]) == nb_zeros(xs[:i + 1]) and len(xs) - i == oude_variant # NbZerosNonzero op 1 en 2 en 4
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and len(xs) - i == oude_variant # Z op 1 of Z op 2 of Herschrijven met 3 in 4
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant # Z op 2 of Z op 4
        pass
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant
    assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant
    i = i + 1
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and 0 <= len(xs) - i < oude_variant
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and not i < len(xs)
assert len(xs) <= i <= len(xs) and n == nb_zeros(xs[:i]) # Z op 4
assert i == len(xs) and n == nb_zeros(xs[:i]) # LeAntisym op 1 en 2
assert n == nb_zeros(xs[:len(xs)]) # Herschrijven met 1 in 2
assert n == nb_zeros(xs) # Herschrijven met SliceFull in 1

# Je mag in je assert-opdrachten gebruik maken van de volgende functie:

def nb_zeros(xs):
    return len([x for x in xs if x == 0])
