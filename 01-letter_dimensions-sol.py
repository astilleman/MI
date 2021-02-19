LETTER_HEIGHT_INCHES = 8.5
LETTER_WIDTH_INCHES = 11
MILLIMETER_PER_INCH = 25.4

# convert the inches to millimeters
letter_height_mms = LETTER_HEIGHT_INCHES * MILLIMETER_PER_INCH
# round the number down to one decimal place, remove the line below to see what happens otherwise
letter_height_mms = round(letter_height_mms, 1)

letter_width_mms = LETTER_WIDTH_INCHES * MILLIMETER_PER_INCH
letter_width_mms = round(letter_width_mms, 1)

# convert the numbers to strings so when can concatenate them
print("USA letter dimension in millimeters: " + str(letter_height_mms) + " x " + str(letter_width_mms))
