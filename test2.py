'''
print("OO", end="")
print(3 + 4)

##
# This program prints a table shoing the growth of an investment.
#

# Define constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000.0

# Obtain the number of years of the computation.
numYears = int(input("Enter number of years: "))

# Print the table of balances for each year.
balance = INITIAL_BALANCE
for year in range(1, numYears + 1):
    interest = balance * RATE / 100
    balance = balance + interest
    print("%4d %10.2f" % (year,balance))


original = input("Enter a string: ")

newString = ""
for char in original:
    if char.isupper():
        newChar = char.lower()
    elif char.islower():
        newChar = char.upper()
    else:
        newChar = char
    newString = newString + newChar
print(newString)

##
#  This program creates a new flipped version of a GIF image.
#

from ezgraphics import GraphicsImage

filename = input("Enter the name of the image file: ")

# Load the original image.
origImage = GraphicsImage(filename)

# Create an empty image that will contain the new flipped image.
width = origImage.width()
height = origImage.height()
newImage = GraphicsImage(width, height)

# Iterate over the image and copy the pixels to the new image to
# produce the flipped image.
newRow = height - 1
for row in range(height):
    for col in range(width):
        newCol = col
        pixel = origImage.getPixel(row, col)
        newImage.setPixel(newRow, newCol, pixel)
    newRow = newRow - 1

# Save the new image with a new name.
newImage.save("flipped-" + filename)
'''

j = 3
while j < 500000:
    print("Wow!")
    j += 1

i = 0
while i < 5:
    print('Joepie')

