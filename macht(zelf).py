'''
Ask a user for
a value x (float)
a value n (positive integer)

Write a program, with a while loop, to calculate xn yourself
without using ** or any function from the math module
'''
'''
# zonder input-validatie maar kan je doen als oefening
# in deze context wel betekenisvolle waarde
x = input("Geef waarde voor x: ")
n = input("Geef waarde voor n: ")

while (not str(x).isdigit() and \
        not (str(x)[0] == "-" and str(x)[1:].isdigit())) or \
        str(x).isdigit() and float(x) % int(x) != 0:
    x = input("Geef waarde voor x: ")
while (not str(n).isdigit() and \
        not (str(n)[0] == "-" and str(n)[1:].isdigit())) or \
        str(n).isdigit() and float(n) % int(n) != 0:
    n = input("Geef waarde voor n: ")

macht = 1
counter = 0
x = int(x)
n = int(n)

while counter < abs(n):
    counter = counter + 1
    macht = macht * x
if n < 0:
    macht = 1/ macht

print("x tot de macht n is", macht)'''

# zonder input-validatie maar kan je doen als oefening
# in deze context wel betekenisvolle waarde
x = input("Geef waarde voor x: ")
n = input("Geef waarde voor n: ")


def geldige_invoer(invoer):
    if invoer != "0":
        while (not str(invoer).isdigit() and \
            not (str(invoer)[0] == "-" and str(invoer)[1:].isdigit())) or \
                str(invoer).isdigit() and float(invoer) % int(invoer) != 0:
            invoer = input("Geef een nieuwe invoer: ")


geldige_invoer(x)
geldige_invoer(n)

macht = 1
counter = 0
x = int(x)
n = int(n)

while counter < abs(n):
    counter = counter + 1
    macht = macht * x
if n < 0:
    macht = 1/ macht

print("x tot de macht n is", macht)






