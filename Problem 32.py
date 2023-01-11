# Problem 32: https://projecteuler.net/problem=32
# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# Solution: Brute force works fine here. We know we'll never need to check a
# 5 digit product since it would require more than 9 digits to create.
from time import time

stime = time()

solutionSet = set()
for a in range(1, 100):
    stra = str(a)
    for b in range(100, 10000):
        strb = str(b)
        product = a*b
        check = list()
        for digit in stra + strb + str(product):
            check.append(int(digit))
        if sorted(check) == sorted(range(1, 10)):
            solutionSet.add(product)

etime = time()
elapsed = round(1000 * (etime - stime), 3)

print(solutionSet)
print(f"Elapsed time={elapsed} milliseconds")
print(f"There are {len(solutionSet)} pandigital products. Their sum is {sum(solutionSet)}")
