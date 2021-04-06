##
#  Read a height map and display which portions of it are covered in water
#  given a flood height.
#

# Define constant variables.
WIDTH = 3
HEIGHT = 3
NUM_LEVELS = 10

def main() :
   heights = []

   # Read all of the height values from the user.
   for i in range(0, HEIGHT) :
      heights.append([])
      for j in range(0, WIDTH) :
         level = float(input("Enter the value for row %d column %d: " % (i, j)))
         heights[i].append(level)

   # Display the map for 10 different flood levels.
   for level in range(0, NUM_LEVELS) :
      print("Water level:", level)
      floodMap(heights, level)
      print()

## Draw a flood map for a certain water level.
#  @param heights a table of terrain heights
#  @param waterLevel a flood level for the terrain
#
def floodMap(heights, waterLevel) :
   for i in range(0, HEIGHT) :
      for j in range(0, WIDTH) :
         if heights[i][j] <= waterLevel :
            print("*", end=" ")
         else :
            print(" ", end=" ")
      print()

# Call the main function.
main()

