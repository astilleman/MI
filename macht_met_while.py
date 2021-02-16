'''
Ask a user for
a value x (float)
a value n (positive integer)

Write a program, with a while loop, to calculate xn yourself
without using ** or any function from the math module
'''

# zonder input-validatie maar kan je doen als oefening
# in deze context wel betekenisvolle waarde
x = float(input("Geef waarde voor x: "))
n = int(input("Geef waarde voor n: "))

'''while n < 0:
    print("Geen geldige waarde! Voer een positieve waarde in!")
    n = int(input("Geef een waarde waarvan dwe de faculteit gaan berekenen: "))'''

macht = 1
counter = 0

while counter < n:
    counter = counter + 1
    macht = macht * x

print("x tot de macht n is", macht)