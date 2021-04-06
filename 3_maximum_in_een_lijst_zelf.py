"""
Schrijf met behulp van een while lus een programma dat het grootste element in een lijst van getallen berekent.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.

Extra:Wat gebeurt er als er zowel integers als strings in je lijst kunnen zitten?
Hoe zou je je preconditie uitbreiden om dit probleem te voorkomen?
"""
lijst = [34.2,7,9,2,-5,1.98,23,-42,28.7,-1,-19,34.3, -3.10]
# Bewijs totale correctheid.
assert 1 <= len(lijst) # 1. P (preconditie)
assert 1 <= 1 <= len(lijst) and lijst[0] == max(lijst[:1]) #Ok, want 1<= len(lijst), 1 <= 1 is eigenschap gehele getallen
# en lijst[0] == max(lijst[:1]), want in een lijst met 1 element, is dat ene element het grootst
i = 1
assert 1 <= i <= len(lijst) and lijst[0] == max(lijst[:i])
max_ = lijst[0]
assert 1 <= i <= len(lijst) and max == max(lijst[:i])
while i < len(lijst):
    oude_variant = len(lijst) - i
    assert 1 <= i <= len(lijst) and max == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant
    if lijst[i] > max_:
        assert 1 <= i <= len(lijst) and max == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and lijst[i] > max
        assert 1 <= i + 1 <= len(lijst) and lijst[i] == max(lijst[:i + 1]) and 0 <= len(lijst) - 1 < oude_variant
        #Ok, want 1 <= i <= len(lijst) en i < len(lijst)
        # => 1 <= i + 1 <= len(lijst) en max == max(lijst[:i]) => max == max(lijst[:i + 1]), wegens definitie maximum
        max_ = lijst[i]
        assert 1 <= i + 1 <= len(lijst) and max == max(lijst[:i + 1]) and 0 <= len(lijst) - 1 < oude_variant

    else:
        assert 1 <= i <= len(lijst) and max == max(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and not lijst[i] > max
        assert 1 <= i + 1 <= len(lijst) and max == max(lijst[:i + 1]) and 0 <= len(lijst) - 1 < oude_variant
        #Ok, want 1 <= i <= len(lijst) en i < len(lijst)
        # => 1 <= i + 1 <= len(lijst) en max == max(lijst[:i]) => max == max(lijst[:i + 1]), wegens definitie maximum
        pass
        assert 1 <= i + 1 <= len(lijst) and max == max(lijst[:i + 1]) and 0 <= len(lijst) - 1 < oude_variant

    assert 1 <= i + 1 <= len(lijst) and max == max(lijst[:i + 1]) and 0 <= len(lijst) - 1 < oude_variant
    i+=1
    assert 1 <= i <= len(lijst) and max == max(lijst[:i]) and 0 <= len(lijst) - 1 < oude_variant
assert 1 <= i <= len(lijst) and max == max(lijst[:i]) and not i < len(lijst)
assert max_ == max(lijst) # 1. Q (postconditie) # 1 <= i <= len(lijst) en not i < len(lijst)
# => 1 <= i <= len(lijst) en i >= len(lijst) => i == len(lijst) en dus max == max(lijst[:i]) => max == max(lijst)
print(max)

