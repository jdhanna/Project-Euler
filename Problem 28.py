# Problem 28: https://projecteuler.net/problem=28
# Starting with 1 and moving to the right in a clockwise direction, a 5 by 5 spiral is formed.
# It can be verified that the sum of the numbers on the diagonals is 101: 21 + 7 + 1 + 3 + 13 + 25 + 9 + 5 + 17
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Solution: No need to go to the trouble of making the spiral, the image clearly shows the pattern the numbers will be added.
def diagonalSum(n):
    #First find the corner numbers on
    def layerCorners(start, layerSize):
        d = layerSize - 1
        return (start + d, start + (2*d), start + (3*d), start + (4*d))


    ans = 1
    start = 1
    for i in range(3,n+1, 2):
        newCorners = layerCorners(start, i)
        ans = ans + sum(newCorners)
        start = newCorners[3]
    return ans

print(f"For a 5x5 integer spiral, the sum of the diagonals is {diagonalSum(5)}")
print(f"For a 1001x1001 integer spiral, the sum of the diagonals is {diagonalSum(1001)}")


