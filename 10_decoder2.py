"""
Schrijf een programma dat een geëncodeerde string ontcijfert.
De string is op volgende manier geëncodeerd:
- De "word characters" zijn x aantal plaatsen naar rechts geshift in het alfabet (e.g. "ac" & shift = 4 --> "eg") (Dit is een caesar cijfer)
- Na elk character van deze nieuwe string werd een "nonsens" character toegevoegd (e.g. "hallo!" --> "h5awlplzo;!à")
- Deze nieuw bekomen string wordt ten slotte omgedraaid.

Hint: maak gebruik van de ASCII waardes van characters om het Caesarcijfer te ontsleutelen.
Hint: maak gebruik van de ord=en =hr=functies voor de ASCII conversies.

Voorbeelden:
"pfyfxa! xfbe" en verschuiving = 1 --> "de zee"
"sepwpoexl" en verschuiving = 4 --> "hallo"
"!!sepwpoexL" en verscuiving = 4 --> "Hallo!"
"""