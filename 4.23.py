# Initialisation

from random import randint

size = randint(10, 100)
computer_starts = randint(0, 1)
smart = randint(0, 1)
size_list = [size]
result = ""


# Game
if computer_starts == 0:
    while size > 0:
        # Human
        amount = int(input("Give a number of marbles: "))
        while amount > size:
            amount = int(input("Not valid. Give another number of marbles: "))
        size -= amount
        if size == 0:
            result = "Computer wins"
            break
        size_list.append(size)

        # Computer
        if smart == 0 or size in [3, 7, 15, 31, 63]:
            amount = randint(1, size//2)
            size -= amount
        else:
            while size not in [3, 5, 15, 31, 63] and size >= 0:
                size -= 1
        if size == 0:
            result = "Human wins"
            break
        size_list.append(size)
    if result == "":
        result = "Computer wins"
#Next moves
else:
    while size > 1:
        # Computer
        if smart == 0 or size in [3, 7, 15, 31, 63]:
            amount = randint(1, size//2)
            size -= amount
        else:
            while size not in [3, 5, 15, 31, 63] and size >= 0:
                size -= 1
        if size == 0:
            result = "Human wins"
        size_list.append(size)
        # Human
        amount = int(input("Give a number of marbles: "))
        while amount > size:
            amount = int(input("Not valid. Give another number of marbles: "))
        size -= amount
        if size == 0:
            result = "Computer wins"
        size_list.append(size)
    if result == "":
        result = "Human wins"

print(computer_starts)
print(smart)
print(result)
print(size_list)