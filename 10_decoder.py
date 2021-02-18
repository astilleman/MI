"""
Schrijf een programma dat een geëncodeerde string ontcijfert.
De string is op volgende manier geëncodeerd:
- De "word characters" zijn x aantal plaatsen naar rechts geshift in het alfabet (e.g. "ac" & shift = 4 --> "eg") (Dit is een caesar cijfer)
- Na elk character van deze nieuwe string werd een "nonsens" character toegevoegd (e.g. "hallo!" --> "h5awlplzo;!à")
- Deze nieuw bekomen string wordt ten slotte omgedraaid.

Hint: maak gebruik van de ASCII waardes van characters om het Caesarcijfer te ontsleutelen.
Hint: maak gebruik van de ord=en =hr=functies voor de ASCII conversies.

Voorbeelden:
"ebfx !axfyfp" en verschuiving = 1 --> "de zee"
"sepwpoexl" en verschuiving = 4 --> "hallo"
"!!sepwpoexL" en verscuiving = 4 --> "Hallo!"
"""

# Ask input from user
word = input("Geef het te decoderen woord: ")
shift_factor = int(input("Geef de verschuivingsfactor weer: "))

# Reverse word
word_reversed = word[::-1]

# Remove nonsense characters
no_nonsense_word = ""
for i in range(len(word_reversed)):
    if i % 2 == 0:
        no_nonsense_word += word_reversed[i]

# Unshifting
# Pas op! De word charachters zijn x aantal plaatsen naar rechts geshift
# in het alfabet staat eerst maar we doen alles in omgekeerde volgorde en dus
# moeten we ook naar links opschijven om oorsprongelijke woord te bekomen
# en is het dus - shift_factor i.p.v. + shift_factor
decoded_word = ""
for letter in no_nonsense_word:
    decoded_word += chr(ord(letter) - shift_factor)

# Print result
#print(word)
#print(word_reversed)
#print(no_nonsense_word)
print("Gedecodeerd woord:", decoded_word)