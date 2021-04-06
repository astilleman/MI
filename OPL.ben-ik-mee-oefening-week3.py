###############################################
#
# Een mogelijke oplossing voor oefening 1
#

numbers = [2, 4, -3, -5, 7, 9, -8, 10]
negative = []

index = 0
while index < len(numbers):
    if numbers[index] < 0:
        negative.append(numbers[index])
        del numbers[index]
    else:
        index += 1

print(numbers)
print(negative)


###############################################
#
# Een mogelijke oplossing voor oefening 3
#

SIZE = 8
matrix = [[0] * x + [1] + [0] * (8 - x - 1) for x in range(SIZE)]
print(matrix)


###############################################
#
# Een eenvoudige 'selection sort'-implementatie (extra oefening)
#

numbers = [2, 4, -3, -5, 7, 9, -8, 10]

for swap_position in range(len(numbers)):
    for following_index in range(swap_position + 1, len(numbers)):
        if numbers[swap_position] > numbers[following_index]:
            numbers[swap_position], numbers[following_index] = numbers[following_index], numbers[swap_position]

print(numbers)
