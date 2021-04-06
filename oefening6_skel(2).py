"""
Schrijf drie functies die als input twee 
strings heeft en als output respectievelijk:
1) een set met alle hoofdletters en kleine 
   letters die in beide strings zitten
2) een set met alle hoofdletters en kleine 
   letters die in geen van beide strings zitten
3) een set met alle niet-letter tekens 
   die in beide strings zitten
"""

def hoodletter_en_kleineletter(string1, string2):
    set_string1 = set(string1)
    set_string2 = set(string2)
    hoofdletterset = set()
    kleineletterset = set()
    set_grote_string = set_string1.union(set_string2)
    for letter in set_grote_string:
        if letter.isalpha(): #MOET ER STAAN
            if letter == letter.lower():
                kleineletterset.add(letter)
            else:
                hoofdletterset.add(letter)
    return kleineletterset, hoofdletterset

print(hoodletter_en_kleineletter("HalloikOPpj", "HalloPj"))
print(hoodletter_en_kleineletter("kdsjfsdlfjqsu!(!çASDFSDFt@)", "fksdfjslkdfj$*MO+d"))

def niet_voorkomende_hoodletter_en_kleineletter(string1, string2):
    kleine_letters_alfabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    hoofd_letters_alfabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    verschil_set_kleine_letters = kleine_letters_alfabet.difference(hoodletter_en_kleineletter(string1, string2)[0])
    verschil_set_hoofd_ketters = hoofd_letters_alfabet.difference(hoodletter_en_kleineletter(string1, string2)[1])
    return verschil_set_kleine_letters, verschil_set_hoofd_ketters

print(hoodletter_en_kleineletter("HalloikOPpj", "HalloPj")[0])
print(niet_voorkomende_hoodletter_en_kleineletter("HalloikOPpj", "HalloPj"))
print(niet_voorkomende_hoodletter_en_kleineletter("kdsjfsdlfjqsu!(!çASDFSDFt@)", "fksdfjslkdfj$*MO+d"))

def niet_letters(string1, string2):
    niet_letter_set = set()
    alle_karakters_set = set(string1).union(set(string2))
    for karakter in alle_karakters_set:
        if not karakter.isalpha():
            niet_letter_set.add(karakter)
    return niet_letter_set

print(niet_letters("kdsjfsdlfjqsu!(!çASDFSDFt@)", "fksdfjslkdfj$*MO+d"))