##
# Computes the number of tiles needed and the gap at each end when
# placing tiles along a wall.
#

# Define the dimensions.
TOTAL_WIDTH = 100
TILE_WIDTH = 5

# Calculate the tiles and gaps.
number_of_pairs = (TOTAL_WIDTH - TILE_WIDTH) // (2 * TILE_WIDTH)
number_of_tiles = 1 + 2 * number_of_pairs
gap = (TOTAL_WIDTH - number_of_tiles * TILE_WIDTH) / 2.0

print("Number of tiles:", number_of_tiles)
print("Gap at each end:", gap)