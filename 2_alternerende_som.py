"""
Schrijf een programma dat de alternerende som van elementen in een lijst berekent.
Bijvoorbeeld als je programma input
    [1, 4, 9, 16, 9, 7, 4, 9, 11]
krijgt dan berekent het
    1 − 4 + 9 − 16 + 9 − 7 + 4 − 9 + 11 = −2
    
Je mag de lijst hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.
"""

# Input
lijst = [1, 4, 9, 16, 9, 7, 4, 9, 11]

# Initialisation
sum = 0

# Calculation
for i in range(len(lijst)):
    if i % 2 == 0:
        sum += lijst[i]
    else:
        sum -= lijst[i]

# Print result
print(sum)