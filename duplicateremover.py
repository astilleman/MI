# indices 0    1    2    3    4    5    6
lijst = ["A", "B", "C", "A", "A", "B", "D"]

# lus nodig, want we moeten elk element van lijst overlopen
# Met while-lus over volledige lijst lopen, typisch zeer vaak gebruikt patroon
# Variabele initialiseren in begin lijst dus op index 0
# We lopen verschillende keren door list en doen telkens + 1
current_index = 0
while current_index < len(lijst):
    # Bepaald element uit lijst halen en dan locatie van dit element in de lijst zoeken.
    # current_index = index waar we momenteel mee bezig zijn,  i = index waar die waarde de 1ste keer in de lijst voorkomt
    current_element = lijst[current_index]

    i = lijst.index(current_element)
    # Duplicaten opsporen en ze verwijderen
    # Door element te verwijderen, zijn indices van volgende elementen al 1 keer verkleind
    # niet i maar current_index
    if current_index != i:
        del lijst[current_index]

    # print(current_element, current_index, i)
    # nodig om stapgsgewijze door lijst te lopen
    # Als we 1 element verwijderen in lijst, worden alle elementen die achter dit element stonden opgeschoven
    # en veranderen ze dus van index
    # Als  we een element verwijderen mogen we de current_index += 1 niet doen
    # Met del hebben we ervoor gezorgd dat de elementen die we moetne bekijken 1tje van index verminderd zijn
    # Dus ELSE
    else:
        current_index += 1








print(lijst) # output ['A', 'B', 'C', 'D']