"""
Schrijf een programma dat als input een getal tussen 1 en 10 krijgt en als output dit getal voluit schrijft. Gebruik hiervoor een dictionary.
"""
# Ask input from user
input = int(input("Give a number:" ))

# Programma
dictionary = {1: "één", 2: "twee", 3: "drie", 4: "vier", 5: "vijf", 6: "zes", 7: "zeven", 8: "acht", 9: "negen", 10: "tien"}
print(dictionary[input])