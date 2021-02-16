'''
‘Zelfde teken…’
Lees 2 float-getallen in
Schrijf uit of beide getallen hetzelfde teken hebben
(test dit via booleaanse uitdrukkingen, niet door beide te vermenigvuldigen)

'''

# input
getal1 = float(input("Enter number one: "))
getal2 = float(input("Enter number two: "))


# signverification
if (getal1 <= 0 and getal2 <= 0) or (getal1 >= 0 and getal2 >= 0):
    print("Beide getallen", getal1, "en", getal2, "hebben hetzelfde teken.")
else:
    print("Beide getallen", getal1, "en", getal2, "hebben een tegengesteld teken")