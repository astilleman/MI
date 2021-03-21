"""
Schrijf met behulp van een while lus een programma dat alle dubbele voorkomens uit een lijst verwijdert.
Je mag de lijst rechtstreeks in het geheugen plaatsen.
Bewijs de correctheid.
"""
lijst1 = [1,2,3,4,5,4,3,3,2,8,1,7]
lijst2 = ["Troye", "Hayley", "Daya", "Trixie", "Years", "Years", "Daya", 2, 5, 2] #Dit gaat even goed met strings als met getallen
lijst = lijst1
i = 0

while i < len(lijst):
	if lijst[i] in lijst[0:i]:
		del lijst[i]
	else:
		i += 1
print(lijst)
