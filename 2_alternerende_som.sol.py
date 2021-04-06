"""
Schrijf een programma dat de alternerende som van elementen in een lijst berekent.
Bijvoorbeeld als je programma input
    [1, 4, 9, 16, 9, 7, 4, 9, 11]
krijgt dan berekent het
    1 − 4 + 9 − 16 + 9 − 7 + 4 − 9 + 11 =−2

Je mag de lijst hier direct in het geheugen plaatsen en hoeft deze dus niet in te lezen.
"""
lijst = [1, 4, 9, 16, 9, 7, 4, 9, 11]

alternerende_som = 0
for i in range(len(lijst)):
    if i % 2 == 0:
        alternerende_som += lijst[i]
    else:
        alternerende_som -= lijst[i]

print("De alternerende som is " + str(alternerende_som))