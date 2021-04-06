
# Ask input from user
amount_in_cents = input("Give an amount in cents: ")
while not str(amount_in_cents).isdigit():
    amount_in_cents = input("Invalid input. Give an amount in cents: ")
amount_in_cents = int(amount_in_cents)

# Conversion to euros
integer_eur = amount_in_cents // 100
cents = amount_in_cents % 100

# Print
print(integer_eur, "EUR")
print("%4s" % cents, "cts")
