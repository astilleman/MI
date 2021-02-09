nb_guests = 20
nb_drinks_per_guest = 2
price_per_drink = 0.35

total_nb_drinks = nb_guests * nb_drinks_per_guest
total_price = price_per_drink * total_nb_drinks

print("This party will cost you " + str(total_price) + "$." )
