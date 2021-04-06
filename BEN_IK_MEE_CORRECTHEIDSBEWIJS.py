from random import random
getal1 = random()
getal2 = random()
getal3 = random()
if getal1 >= getal3 and getal2 >= getal3:
    min = getal3
elif getal1 >= getal2 and getal3 >= getal2:
    min = getal2
else:
    min = getal1
print(getal1, getal2, getal3, min)
