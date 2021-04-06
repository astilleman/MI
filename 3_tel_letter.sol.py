"""
Definiëer een functie die telt hoe vaak een gegeven letter in een 
string voorkomt. De functie moet altijd een geheel getal teruggeven. 

Onderaan de file staan enkele 'assert' statements.
Wanneer je deze file runt, zullen die ook uitgevoerd worden 
en weet je of jeimplementatie al dan niet correct is.
"""

def tel_letter(letter, string):
    count =0
    for l in string:
        if l==letter:
            count+=1
    return count

# TESTS
assert tel_letter('e', "methodiek van de informatica") == 3
assert tel_letter('t',"hottentottententententoonstelling") == 10
assert tel_letter('a', "python") == 0

