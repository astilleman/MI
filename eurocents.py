# This program will convert an amount in eurocents into EUR and remaining cents
# altijd betekenisvolle namen gebruiken

amount_in_cents = 834234
amount_in_EUR = amount_in_cents // 100
remaining_amount_in_cents = amount_in_cents % 100

print(amount_in_EUR ,"EUR")
print(remaining_amount_in_cents)

from math import trunc
print(trunc(5.4))
print(trunc(5.55))
print(trunc(5))