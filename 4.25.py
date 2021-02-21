## 3 doors and a car problem

from random import randint

# Initialisation
counter1 = 0
counter2 = 0

# Ask input from user
for i in range(1000):
    car_door = randint(1, 3)
    chosen_door1 = randint(1, 3)
    if chosen_door1 == car_door:
        counter2 += 1
    else:
        door_gameshow = randint(1, 3)
        while door_gameshow == chosen_door1 or door_gameshow == car_door:
            door_gameshow = randint(1, 3)
        #chosen_door2 = randint(1, 3)
        #while chosen_door2 == door_gameshow:
            #chosen_door2 = randint(1, 3)
        #if chosen_door1 == chosen_door2 == car_door:
            #counter2 += 1
        #elif chosen_door1 != chosen_door2 and chosen_door2 == car_door:
            #counter1 += 1
        # DUSSSS niet meer werkelijk 2e deur kiezen, maar kijken wat
        # er gebeurt als speler blijft of verplaatst.
        if chosen_door1 == car_door:
            counter2 += 1
        else:
            counter1 += 1
# Print result
print("Counter 1:", counter1, "\nCounter 2:", counter2)

