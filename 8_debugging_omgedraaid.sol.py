"""
De functie reverse_tuple zou een tuple moeten teruggeven 
dat dezelfde elementen bevat als de input tuple maar dan 
in de omgekeerde volgorde. Helaas zijn er enkele bugs in 
het programma geslopen. Kan jij ze vinden? Lees de errors 
en gebruik de built-in debugger van Pycharm om de foutjes 
te vinden en te corrigeren.
"""

def reverse_tuple(tuple):
    # Fout 1: Er was geen base case die een lege tuple afhandelde.
    if len(tuple) <= 1:
        return tuple
    else:
        # Fout 2: Het eerste element werd vooraan toegevoegd i.p.v. achteraan.
        # Fout 3: De syntax was incorrect voor tuples met lengte 1.
        # Fout 4: Er werd altijd de volledige tuple meegegeven als input aan de recursieve oproep.
        reversed_tuple = reverse_tuple(tuple[1:]) + (tuple[0],)
        return reversed_tuple

assert reverse_tuple(()) == ()
assert reverse_tuple((4,)) == (4,)
assert reverse_tuple((4, 6)) == (6, 4)
