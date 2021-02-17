"""
Write a program that displays the dimensions of a US letter size (8.5x11 inch) sheet of
paper in millimeters. There are 25.4 millimeters per inch. Use constants in your program.

Example output:
    USA letter dimensions in millimeters: 215.9 x 279.4

Hint: if you want to round a number to x digits after the comma, use round(number,x)
"""

# constant values
PAPER_WIDTH_INCH = 8.5
PAPER_HEIGHT_INCH = 11
INCH_TO_MM = 25.4

# Calculation format paper in mm
paper_width_mm = round(PAPER_WIDTH_INCH * INCH_TO_MM, 1)
paper_height_mm = round(PAPER_HEIGHT_INCH * INCH_TO_MM, 1)

# Print in correct format
print("USA letter dimension in millimeters:", paper_width_mm, "x", paper_height_mm)