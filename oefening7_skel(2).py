"""
Gegeven volgende dictionary:
        {"Algemene en Technische Scheikunde":"H01A8A"
        , "Toegepaste Mechanica Deel 1":"H01B0B"}
1)Voeg het vak Methodiek van de Informatica toe aan deze dictionary
2) Vraag de code van het vak Algemene en Technische Scheikunde op
"""

dictionary= {"Algemene en Technische Scheikunde":"H01A8A", "Toegepaste Mechanica Deel 1":"H01B0B"}

dictionary["Methodiek van de Informatica"] = "H01B6B"
code_ATS = dictionary["Algemene en Technische Scheikunde"]

print(dictionary)
print(code_ATS)