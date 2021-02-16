'''
‘Mini-analyse van de leeftijd van een person’
Vraag naar leeftijd
Input-validatie
getal moet tussen 0 en 134 zijn.
Schrijf uit in welk jaar de persoon is geboren, en of hij/zij meerderjarig is.

'''
THIS_YEAR = 2021

age = int(input("Geef leeftijd: "))
while age < 0 or age > 134:
    print(" Dit is geen gelidige leeftijd, probeer opnieuw")
    age = int(input("Geef leeftijd: "))

# Na while-lus sws geldig getal

year_of_birth = THIS_YEAR - age
print("Year of birth is", year_of_birth)
if age >= 10:
    print("The person is not a minor")
else:
    print("The person is a minor")