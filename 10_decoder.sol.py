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
# encryptedSentence = "sepwpoexL" 4
reversed_encrypted_sentence = input("Geef het te decoderen woord: ")
shift = int(input("Geef de verschuivingsfactor weer: "))

# Keer het woord om:
encrypted_sentence = ""
for i in reversed_encrypted_sentence:
    encrypted_sentence = i + encrypted_sentence
# Kortere manier:
# encrypted_sentence = reversed_encrypted_sentence[::-1]

print("Gedecodeerd woord: ", end="")
for i in range(0, len(encrypted_sentence), 2):
    if encrypted_sentence[i].isalpha():
        if encrypted_sentence[i].islower():
            first_letter = 'a'
        else:
            first_letter = "A"

        alphabet_number = ord(encrypted_sentence[i]) - ord(first_letter) - shift
        new_number = alphabet_number % 26 + ord(first_letter)
        print(chr(new_number), end="")
    else:
        print(encrypted_sentence[i], end="")
