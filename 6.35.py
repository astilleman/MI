from math import sqrt
from time import sleep
from random import randint
def floodMap(heights, waterLevel):
    side_square = int(sqrt(len(heights)))
    for i in range(side_square):
        for j in range(i*side_square,i*side_square + side_square):
            if heights[j] > waterLevel:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def flooded_in_time_reversed(heights, steps):
    lowest_height = min(heights)
    maximum_height = max(heights)
    for i in range(10):
        floodMap(heights, lowest_height + (maximum_height-lowest_height)*(i/9))
        sleep(5)

def flooded_in_time(heights):
    lowest_height = min(heights)
    maximum_height = max(heights)
    side_square = int(sqrt(len(heights)))
    for i in range(10):
        for j in range(side_square):
            for k in range(j*side_square,j*side_square + side_square):
                if heights[k] <= lowest_height + (i/9)*(maximum_height/lowest_height):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        sleep(3)
        print()


flooded_in_time([randint(1, 20) for v in range(100)])