"""
Schrijf een programma dat een decimaal getal omzet naar binaire vorm.
"""
'''
# Ask input from user
number = int(input("Geef een positief geheel getal in: "))

# Transformation to binary code
binary_number = bin(number)

# Print result
print(binary_number)
'''

# Zelf code en niet ingebouwde functie gebruiken
# Ask input from user
number = int(input("Geef een positief geheel getal in: "))

# Binary conversion
binary_number = ""
rest = number
while number > 0:
    rest = number % 2
    binary_number += str(rest)
    number = number // 2
binary_code = "0B" + binary_number[::-1]

# Print result
print("De binaire representatie van 0 is: ", binary_code)