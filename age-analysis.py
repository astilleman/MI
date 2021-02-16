'''
‘Mini-analyse van de leeftijd van een person’
Vraag naar leeftijd
Input-validatie
getal moet tussen 0 en 134 zijn.
Schrijf uit in welk jaar de persoon is geboren, en of hij/zij meerderjarig is.

'''
THIS_YEAR = 2021

age = int(input("Geef leeftijd: "))

if age < 0 or age > 134:
    print("Geen geldige leeftijd")
# Hier MOET een else komen
else:
    year_of_birth = THIS_YEAR - age
    print("Year of birth is", year_of_birth)
    if age >= 10:
        print("The person is not a minor")
    else:
        print("The person is a minor")

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")
