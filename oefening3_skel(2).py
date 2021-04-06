"""
In cryptografie is caesar cipher een encryptietechniek
waarin elke letter in het alfabet vervangen wordt door
een letter die een aantal posities verder in het alfabet 
staat. In dit geval implementeren we ROT-13, waarbij elke 
letter dertien plaatsen opschuift. Een a zou bijvoorbeeld 
een n worden. Schrijf hiervoor een encoder en decoder en 
vertaal/codeer hiermee de volgende twee berichten:
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
Gebruik voor deze opgave een dictionary!
"""
# input
tekst = input("Enter text: ")
ontcijferde_tekst = ""
ontcijferdictionary = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l":"y", "m":"z"}

def GetKey(val):
   for key, value in ontcijferdictionary.items():
      if val == value:
         return key

for letter in tekst.lower():
    if letter in ontcijferdictionary:
        ontcijferde_tekst += ontcijferdictionary[letter]
    elif letter in ontcijferdictionary.values():
        ontcijferde_tekst += GetKey(letter)
    else:
        ontcijferde_tekst += letter
print(ontcijferde_tekst)



