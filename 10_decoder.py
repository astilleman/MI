"""
Schrijf een programma dat een geëncodeerde string ontcijfert.
De string is op volgende manier geëncodeerd:
- De "word characters" zijn x aantal plaatsen naar rechts geshift in het alfabet (e.g. "ac" & shift = 4 --> "eg") (Dit is een caesar cijfer)
- Na elk character van deze nieuwe string werd een "nonsens" character toegevoegd (e.g. "hallo!" --> "h5awlplzo;!à")
- Deze nieuw bekomen string wordt ten slotte omgedraaid.

Hint: maak gebruik van de ASCII waardes van characters om het Caesarcijfer te ontsleutelen.
Hint: maak gebruik van de ord=en =hr=functies voor de ASCII conversies.

Voorbeelden:
"ebfx !axfyfp" en verschuiving = 1 --> "de zee" (vervangen door pfyfxa! xfbe en 1)
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
    # enkel oorspronkelijke letters moeten opgeschoven worden
    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        if letter.isupper():
            if (ord(letter) - shift_factor) < 65:
                decoded_word += chr(ord(letter) - shift_factor - 65 + 91)
            else:
                decoded_word += chr(ord(letter) - shift_factor)
        elif letter.islower():
            if 90 < (ord(letter) - shift_factor) < 97:
                decoded_word += chr(ord(letter) - shift_factor - 97 + 123)
            else:
                decoded_word += chr(ord(letter) - shift_factor)
    else:
        decoded_word += letter



'''
if encrypted_sentence[i].isalpha():
if encrypted_sentence[i].islower():
first_letter = 'a'
else:
first_letter = "A"

for letter in no_nonsense_word:
    if (letter.lower()).isalpha():
        if letter 
        decoded_word += chr(ord(letter) - shift_factor)
    else:
        decoded_word += letter
'''


# Print result
print(word)
print(word_reversed)
print(no_nonsense_word)
print("Gedecodeerd woord:", decoded_word)