"""
Schrijf met behulp van een while lus een programma dat alle dubbele voorkomens uit een lijst verwijdert.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.
"""

# Helpfunctie (om code te compilen).

def correcte_verwijder_dubbels_functie(lijst):
    return list(dict.fromkeys(lijst))
lijst1 = [1,2,3,4,5,4,3,3,2,8,1,7]
lijst2 = ["Troye", "Hayley", "Daya", "Trixie", "Years", "Years", "Daya", 2, 5, 2] #Dit gaat even goed met strings als met getallen

# Bewijs totale correctheid
lijst = lijst1
i = 0
assert 1 < len(lijst) # 1. P
assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) #3. Ok i == 0 dus 0<= i len(lijst) > 1 dus len(lijst) >= i >= 0
while i < len(lijst):
    oude_variant = len(lijst) - i
    assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant
    if lijst[i] in lijst[0:i]:
      assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and lijst[i] in lijst[0:i]
      del lijst[i]
      assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and 0 <= len(lijst) < oude_variant #2. naar boven propaggeren
    else:
      assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and i < len(lijst) and len(lijst) - i == oude_variant and not lijst[i] in lijst[0:i]
      assert 0 <= i+1 <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i+1]) and 0 <= len(lijst) < oude_variant
      # #2. naar boven propaggeren 3.Ok 0 <= i <= len(lijst) en i < len(lijst) => 0 <= i+1 <= len(lijst)
      i += 1
      assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and 0 <= len(lijst) < oude_variant #2. naar boven propaggeren
    assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and 0 <= len(lijst) < oude_variant #2. naar boven propaggeren
assert 0 <= i <= len(lijst) and lijst == correcte_verwijder_dubbels_functie(lijst[:i]) and not i < len(lijst)
assert lijst == correcte_verwijder_dubbels_functie(lijst) # 1. Q #3. Ok, letterlijk overnemen
print(lijst)