"""
Schrijf een functie die als 
input een zin/meerdere 
zinnen krijgt en een set teruggeeft 
met alle woorden in de tekst. 
"""


# Deze functie verwijdert alle speciale tekens van de zin
def nospecial(text):
    import re
    text = re.sub("[^a-zA-Z0-9 ]+", "", text)
    return text

def woorden_tekst(tekst):
    woorden = nospecial(tekst).split(" ")
    return set(woorden)

print(woorden_tekst("Hallo mijn naam is Anne-Sophie, hallo mijn naam is Louis"))