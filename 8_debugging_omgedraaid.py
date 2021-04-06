"""
De functie reverse_tuple zou een tuple moeten teruggeven 
dat dezelfde elementen bevat als de input tuple maar dan 
in de omgekeerde volgorde. Helaas zijn er enkele bugs in 
het programma geslopen. Kan jij ze vinden? Lees de errors 
en gebruik de built-in debugger van Pycharm om de foutjes 
te vinden en te corrigeren.
"""

def reverse_tuple2(tuple):
    if len(tuple) == 1:
        return tuple
    else:
        reversed_tuple = tuple[0] + reverse_tuple(tuple)
        return reversed_tuple

def reverse_tuple(tuple):
    if len(tuple) == 0: #or len(tuple) == 1:
        return tuple
    else:
        # speciale notatie python ,) anders leest python dit niet als tuple
        reversed_tuple = (tuple[-1],) + reverse_tuple(tuple[0:len(tuple) - 1])
        #reversed_tuple = tuple[0:len(tuple)]
    return reversed_tuple

assert reverse_tuple(()) == ()
assert reverse_tuple((4,)) == (4,)
assert reverse_tuple((4, 6)) == (6, 4)
