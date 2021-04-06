"""
Een palindroom is een string die hetzelfde leest van links naar 
rechts, als omgekeerd. Enkele voorbeelden van palindromen zijn: 
    - kayak
    - racecar
    - was it a cat I saw

Schrijf een recursieve functie die een string vraagt aan de gebruiker en 
nakijkt of deze string al dan niet een palindroom is. Indien de 
ingevoerde string een palindroom is, moet de functie True teruggeven, 
anders geeft de functie False terug.

Je mag ervan uitgaan dat de gegeven string geen spaties bevat.

Let op: Zorg ervoor dat je functie niet hoofdlettergevoelig is.
"""

def is_palindroom(string):
	if not string:
		return True
	elif len(string) == 1:
		return True
	else:
		if string[0].lower() == string[-1].lower():
			return is_palindroom(string[1:-1])
		else:
			return False


# TESTS
assert is_palindroom("")
assert is_palindroom("a")
assert is_palindroom("aa")
assert not is_palindroom("ab")
assert is_palindroom("aba")
assert not is_palindroom("aab")
assert is_palindroom("kayak")
assert not is_palindroom("racehorse")
assert is_palindroom("racecar")
assert is_palindroom("wasitacatIsaw")
assert is_palindroom(123)