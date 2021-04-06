"""
Schrijf met behulp van een while lus een programma dat alle dubbele voorkomens uit een lijst verwijdert.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.
"""
lijst1 = [1,2,3,4,5,4,3,3,2,8,1,7]
lijst2 = ["Troye", "Hayley", "Daya", "Trixie", "Years", "Years", "Daya", 2, 5, 2] #Dit gaat even goed met strings als met getallen
lijst = lijst1

assert 0 <= len(lijst)
assert 0 <= 0 <= len(lijst) and len(lijst[:0]) == len(set(lijst[:0]))
# De eerste expressies in beide assert statements zijn gelijk dus hier moet niet verder over geredeneerd worden.
# De tweede expressie in de tweede assert statement is triviaal waar want de lengte van een
# lege set is gelijk aan die van een lege lijst want deze zijn beiden gelijk aan 0.
i = 0
assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) #LUSINVARIANT: als de lijst dezelfde lengte heeft als de set gemaakt van deze lijst, is elk element uniek
while i < len(lijst):
    oude_variant = len(lijst[i:len(lijst)]) #te behandelen deel van de lijst wordt elke keer korter
    assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and i<len(lijst) and len(lijst[i:len(lijst)]) == oude_variant
    if lijst[i] in lijst[0:i]:
        assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and len(lijst[i:len(lijst)]) == oude_variant and lijst[i] in lijst[0:i]
        del lijst[i]
        assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and 0 <= len(lijst[i:len(lijst)]) < oude_variant
    else:
        assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and len(lijst[i:len(lijst)]) == oude_variant and not lijst[i] in lijst[0:i]
        assert 0 <= i+1 <= len(lijst) and len(lijst[:i+1]) == len(set(lijst[:i+1])) and 0 <= len(lijst[i+1:len(lijst)]) < oude_variant
        # OK want de eerste i elementen van de lijst uniek zijn en het volgende element is uniek is tegenover
        # de eerste i elementen van de lijst (zie laatste conditie in de eerste assert). Hieruit volgt dat
        # de operatie (set(lijst[:i+1])) geen elementen zal verwijderen waardoor de grootte van de set
        # gelijk zal zijn aan de lengte van de lijst.
        i += 1
        assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and 0 <= len(lijst[i:len(lijst)]) < oude_variant
    assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and 0 <= len(lijst[i:len(lijst)]) < oude_variant

assert 0 <= i <= len(lijst) and len(lijst[:i]) == len(set(lijst[:i])) and not i < len(lijst)
assert len(lijst) == len(set(lijst))
# Door i == len(lijst) te substitueren in len(lijst[:i]) == len(set(lijst[:i])) bekomen we
# de postconditie len(lijst) == len(set(lijst)).

print(lijst)