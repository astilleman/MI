################ Deel1
# Input (als zelf moet testen voor geldigheid dan zoals bij 03 inner product zelf gedaan)
numbers = [2, 4, -3, -5, 7, 9, -8, 10]

# Initialisation
negative = []

# We zullen maar 0 positief en negatief nemen
# For-lus lukt niet goed met elementen verwijderen dus while-lus
current_index = 0
while current_index < len(numbers):
    if numbers[current_index] <= 0:
        # Belangrijk om eerst toe te voegen aan negatieve lijst, want anders voeg je
        # foute elementen toe door verandering index
        negative.append(numbers[current_index])
        numbers.remove(numbers[current_index])
    else:
        current_index += 1


# Print result
# Can only concatenate string not list dus type casting
print("numbers = " + str(numbers) + "\n" + "negative = " + str(negative))

############### Deel2
t = ("Bill Gates", 64, 112.8, True, "Seattle, Washington")
# t[-5:2] = ("Bill Gates", 64)
# t[-5:2][-2] = "Bill Gates"
# t[-5:2][-2][5::-1] = "G lliB" != t[-5:2][-2][5:-1:] = "Gate"
print(t[-5:2])
print(t[-5:2][-2])
print(t[-5:2][-2][5::-1])
print(t[-5:2][-2][5:-1:])

############### Deel 3
SIZE = 8
# FOUT
#matrix = [ [0]  if i!=j else [1]  for i in range(SIZE) for j in range(i)]
matrix1= [[int(col == row) for col in range(SIZE)] for row in range(SIZE)]
matrix2 = [[1 if col == row else 0 for col in range(SIZE)] for row in range(SIZE)]
print(matrix1)
print(matrix2)
#[a if a else 2 for a in [0,1,0,3]]
