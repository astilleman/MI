# input
richter = float(input("Give a number on the scale of richter: "))

# Conditions
if richter >= 8.0: # handle the special case first
    print("Most sructures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many builidngs damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed building")
else: # so that the 'general case' can be handled last
    print("No construction of building")