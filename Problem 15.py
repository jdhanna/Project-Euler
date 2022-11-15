# Problem: Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid

# Solution: Calculating the number of routes through a n x m grid is finding the number of permutations of n steps right and m steps down.

import math

def latticePaths(right, down):
    ans = math.comb(right + down, right)
    return ans

print(latticePaths(2,2))
print(latticePaths(20,20))