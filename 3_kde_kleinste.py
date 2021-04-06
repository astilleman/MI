"""
Het Quick Sort algoritme verdeelt een lijst in een deel
kleiner dan en een deel groter dan een pivot element.
Hierdoor is de positie van het pivot element gekend. Deze
opsplitsing kan gebruikt worden om het k-de kleinste element
in een lijst te vinden, door telkens in de correct helft
verder te zoeken. Schrijf een functie die deze strategie
gebruikt om het k-de kleinste element in een lijst te zoeken.
Indien de waarde van k ongeldig is, dan moet de functie -1
terug geven. (Hint: schrijf een aparte functie om de lijst te
partitioneren zoals bij Quick Sort)
"""

def zoek_kde_kleinste(k, lijst):
    if len(lijst) == 0:
        return
    elif len(lijst) == 1:
        return lijst[0]


def partition(values, start, to):
    pivot = values[start]
    i = start+1
    geq = start+1 # op 2 plaatsen lege range in invar dus sws voldaan
    while i != to + 1:
        if values[i] >= pivot:
            pass
        else:
            values[i], values[geq] = values[geq], values[i]
            geq += 1
        i += 1
    geq -= 1 # we komen op laatste element dat strikt kleiner is dan pivot
    values[geq], values[start] = values[start], values[geq]
    return geq


print(zoek_kde_kleinste(6, [4, 15, 5, 3, 5, 11, 8, 12, 19]))
print(zoek_kde_kleinste(9, [18, 8, 0, 12, 7, 6, 5, 2, 1]))
'''
# Tests om te kijken of de implementatie correct is
assert zoek_kde_kleinste(6, [4, 15, 5, 3, 5, 11, 8, 12, 19]) == 11
assert zoek_kde_kleinste(9, [18, 8, 0, 12, 7, 6, 5, 2, 1]) == 18
assert zoek_kde_kleinste(4, [3, 7, 16, 3, 5, 2, 5, 9, 12]) == 5
assert zoek_kde_kleinste(1, [19, 7, 1, 15, 6, 0, 10, 20, 18]) == 0
# De gegeven k is niet gelding indien k <= 0 of k > len(lijst)
assert zoek_kde_kleinste(0, [15, 19, 6, 4, 12, 1, 9]) == -1
assert zoek_kde_kleinste(8, [16, 20, 7, 4, 2, 6, 14]) == -1
'''