# Het programma hieronder telt het aantal keren dat de waarde 0 voorkomt
# in de gegeven lijst xs. Het plaatst het resultaat in variabele n.
# Je mag in je assert-opdrachten gebruik maken van de volgende functie:

def nb_zeros(xs):
    return len([x for x in xs if x == 0])

'''
i = 0
n = 0
while i < len(xs):
    if xs[i] == 0:
        n = n + 1
    else:
        pass
    i = i + 1'''

xs = [0, 1, 3, 4, 6, 0, 0, 10]
# Voorzie dit programma van een gepaste preconditie en postconditie en
# bewijs haar correctheid.

# Voorzie twee bewijzen: één waarbij je partiële correctheid bewijst,
# en één waarbij je totale correctheid bewijst.

# Partiële correctheid:
assert 0 <= len(xs) #PRECONDITIE
assert 0 <= 0 <= len(xs) and 0 == nb_zeros(xs[:0]) # OK! Het eerste deel van de 2de assert is equivalent
# aan de vorige assert en als het aantal nullen in een lijst met nul elementen is uiteraard 0.
i = 0
assert 0 <= i <= len(xs) and 0 == nb_zeros(xs[:i])
n = 0
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) # Lusinvariant
while i < len(xs):
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs)
    if xs[i] == 0:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and xs[i] == 0
        assert 0 <= i + 1 <= len(xs) and n + 1 == nb_zeros(xs[:i + 1]) # OK! Uit 0 <= i <= len(xs) en i < len(xs) volgt dat
        # als we i ééntje vermeerderen, het mogelijks nu wel gelijk kan zijn aan len(xs), dus dat 0 <= i + 1 <= len(xs).
        # Uit n == nb_zeros([xs[:i]]) en xs[i] == 0 volgt dat n + 1 == nb_zeros([xs[:i + 1]]), aangezien het ide element 0 is en
        # dit niet wordt bijgeteld bij n (exclusieve i), moet als je i er bij neemt dus i + 1 exclusief er een nul bijgekomen zijn,
        # dus n + 1 i.p.v. n.
        n = n + 1
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    else:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and not xs[i] == 0
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) # OK! Uit 0 <= i <= len(xs) en i < len(xs) volgt dat
        # als we i eentje vermeerderen het mogelijks nu wel gelijk kan zijn aan len(xs), dus 0 <= i + 1 <= len(xs).
        # Uit n == nb_zeros([xs[:i]]) en not xs[i] == 0 volgt dat n == nb_zeros([xs[:i + 1]]), aangezien het ide element geen
        # 0 is maakt dat het geen verschil uit als we het ide element exclusief of inclusief nemen om het aantal nullen, n, te
        # berekenen.
        pass
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1])
    i = i + 1
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i])
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and not i < len(xs)
assert n == nb_zeros(xs) #POSTCONDITIE # OK! Uit 0 <= i <= len(xs) en not i < len(xs) volgt dat i == len(xs)
# Dit invullen in n == nb_zeros([xs[:i]]) geeft  n == nb_zeros([xs[:len(xs)]]) wat equivalent is met n == nb_zeros(xs)
# en dit is precies de postconditie.

# Totale correctheid:

assert 0 <= len(xs) #PRECONDITIE
assert 0 <= 0 <= len(xs) and 0 == nb_zeros(xs[:0])# OK! Het eerste deel van de 2de assert is equivalent
# aan de vorige assert en als het aantal nullen in een lijst met nul elementen is uiteraard 0.
i = 0
assert 0 <= i <= len(xs) and 0 == nb_zeros(xs[:i])
n = 0
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) # Lusinvariant
while i < len(xs):
    oude_variant = len(xs) - i
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant
    if xs[i] == 0:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant and xs[i] == 0
        assert 0 <= i + 1 <= len(xs) and n+1 == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant #OK!
        # Uit 0 <= i <= len(xs) en i < len(xs) volgt dat
        #als we i ééntje vermeerderen, het mogelijks nu wel gelijk kan zijn aan len(xs), dus dat 0 <= i + 1 <= len(xs).
        #Uit n == nb_zeros([xs[:i]]) en xs[i] == 0 volgt dat n + 1 == nb_zeros([xs[:i + 1]]), aangezien het ide element 0 is en
        #dit niet wordt bijgeteld bij n (exclusieve i), moet als je i er bij neemt dus i + 1 exclusief er een nul bijgekomen zijn,
        #dus n + 1 i.p.v. n.
        # Uit len(xs) - i == oude_variant volgt dat len(xs) - (i + 1) = len(xs) -i - 1 < oude_variant.
        n = n + 1
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant
    else:
        assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and i < len(xs) and len(xs) - i == oude_variant and not xs[i] == 0
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant # OK!
        # Uit 0 <= i <= len(xs) en i < len(xs) volgt dat  als we i eentje vermeerderen het mogelijks nu wel gelijk kan zijn aan
        # len(xs), dus 0 <= i + 1 <= len(xs).
        # Uit n == nb_zeros([xs[:i]]) en not xs[i] == 0 volgt dat n == nb_zeros([xs[:i + 1]]), aangezien het ide element geen
        # 0 is maakt dat het geen verschil uit als we het ide element exclusief of inclusief nemen om het aantal nullen, n, te
        # berekenen.
        # Uit len(xs) - i == oude_variant volgt dat len(xs) - (i + 1) = len(xs) -i - 1 < oude_variant.
        pass
        assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i + 1]) and 0 <= len(xs) - (i + 1) < oude_variant
    assert 0 <= i + 1 <= len(xs) and n == nb_zeros(xs[:i+1]) and 0 <= len(xs) - (i+1) < oude_variant
    i = i + 1
    assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and 0 <= len(xs) - i < oude_variant
assert 0 <= i <= len(xs) and n == nb_zeros(xs[:i]) and not i < len(xs)
assert n == nb_zeros(xs) #POSTCONDITIE # OK! Uit 0 <= i <= len(xs) en not i < len(xs) volgt dat i == len(xs)
# Dit invullen in n == nb_zeros([xs[:i]]) geeft  n == nb_zeros([xs[:len(xs)]]) wat equivalent is met n == nb_zeros(xs)
# en dit is precies de postconditie.

