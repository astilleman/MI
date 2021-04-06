"""
Schrijf met behulp van een while lus een programma dat het grootste element in een lijst van getallen berekent.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.

Extra:Wat gebeurt er als er zowel integers als strings in je lijst kunnen zitten?
Hoe zou je je preconditie uitbreiden om dit probleem te voorkomen?
"""
''''
#eigen functie (extra)
def getal_boolean_functie(lijst):
    for getal in lijst:
        getal = str(getal).replace('.', '')
        if not getal.isdigit() and \
                not(getal[0] == "-" and getal[1:].isdigit()):
            lijst.remove(getal)
#stop mijne
'''
def string_to_int_or_float(lijst):
    nieuwe_lijst = []
    for getal in lijst:
        if type(getal) == str:
            getal = float(getal)
        nieuwe_lijst.append(getal)
    return nieuwe_lijst


lijst = [34.2,7,9,2,-5,1.98,23,-42,28.7,-1, -19,34.3, -3.10]
#getal_boolean_functie(lijst)
#lijst = string_to_int_or_float(lijst)
assert 0 < len(lijst) and all(not(isinstance(element, str)) for element in lijst)
assert 1 <= 1 <= len(lijst) and lijst[0] == max(lijst[:1])
# De twee asserts volgen op elkaar want als 0 < len(lijst),
# dan is de lengte van de lijst minstens 1 en dus geldt 
# 1 <= len(lijst). De tweede uitdrukking in de tweeede assert
# is triviaal waar want in een lijst met 1 element is het enige
# element uiteraard ook het grootste element.
maximum = lijst[0]
assert 1 <= 1 <= len(lijst) and maximum == max(lijst[:1])
i = 1
assert 1 <= i <= len(lijst) and maximum == max(lijst[:i])
while i < len(lijst):
    oude_variant = len(lijst)-i
    assert 1 <= i <= len(lijst) and maximum == max(lijst[:i]) and i < len(lijst) and len(lijst)-i == oude_variant
    if lijst[i] > maximum:
        assert 1 <= i <= len(lijst) and maximum == max(lijst[:i]) and i < len(lijst) and len(lijst)-i == oude_variant and lijst[i] > maximum
        assert 1 <= i + 1 <= len(lijst) and lijst[i] == max(lijst[:i + 1]) and 0 <= len(lijst)-(i+1) < oude_variant
        # Als 1 <= i <= len(lijst) en i < len(lijst) waar zijn, dan geldt dus dat i < len(lijst).
        # Dus indien we i met 1 verhogen, dan kan deze variabele mogelijks weer gelijk zijn aan len(lijst).
        # Lijst[i] is groter dan de maximale waarde in lijst[:i] (lijst[i] > maximum) en het behoort niet tot die slice 
        # maar is wel het element dat daarop volgt. Hieruit volgt duidelijk dat lijst[i] == max(lijst[:i+1]).
        maximum = lijst[i]
        assert 1 <= i + 1 <= len(lijst) and maximum == max(lijst[:i + 1])  and 0 <= len(lijst)-(i+1) < oude_variant
    else:
        assert 1 <= i <= len(lijst) and maximum == max(lijst[:i]) and i < len(lijst) and len(lijst)-i == oude_variant and not lijst[i] > maximum
        assert 1 <= i + 1 <= len(lijst) and maximum == max(lijst[:i + 1])  and 0 <= len(lijst)-(i+1) < oude_variant
        pass
        assert 1 <= i + 1 <= len(lijst) and maximum == max(lijst[:i + 1])  and 0 <= len(lijst)-(i+1) < oude_variant
    assert 1 <= i + 1 <= len(lijst) and maximum == max(lijst[:i + 1]) and 0 <= len(lijst)-(i+1) < oude_variant
    i += 1
    assert 1 <= i <= len(lijst) and maximum == max(lijst[:i]) and 0 <= len(lijst)-i < oude_variant

assert 1 <= i <= len(lijst) and maximum == max(lijst[:i]) and not i < len(lijst)
assert maximum == max(lijst)
# We hebben hier i == len(lijst) en als we dit substitueren in maximum == max(lijst[:i])
# krijgen we de postconditie, namelijk: [maximum == max(lijst[:len(lijst)])] = [maximum == max(lijst)]

print("Het grootste getal in deze lijst is " + str(maximum))


