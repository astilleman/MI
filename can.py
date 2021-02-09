##
# This program prints the price per centi-liter for a six-pack of cans
#

# Define constants for pack size
CANS_PER_PACK = 6

# Get price and volume information from user
user_input = input("Enter price for six-pack: ")
pack_price = float(user_input)

user_input = input("Enter volume for each can (in centi-liter): ")
can_volume = float(user_input)

# Compute pack volume
pack_volume = can_volume * CANS_PER_PACK

# Compute and print price per liter
price_per_cl = pack_price / pack_volume
print("Price per liter: ", price_per_cl * 100)
