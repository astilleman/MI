'''
Ask a user for
a value n (integer)

Write a program, with a while loop, to calculate n!
Write a program, with a for loop, to calculate n!
'''

n = int(input("Geef een waarde waarvan we de faculteit gaan berekenen: "))
originele_n = n

while n < 0:
    print("Geen geldige waarde! Voer een positieve waarde in!")
    n = int(input("Geef een waarde waarvan dwe de faculteit gaan berekenen: "))

faculteit = 1

while n > 0:
    faculteit = faculteit * n
    n = n - 1

print("De faculteit van", originele_n, "is", faculteit)


