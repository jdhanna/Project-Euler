# Problem 32: https://projecteuler.net/problem=32
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# Solution: Brute force works fine here. We know we'll never need to check a 5 digit product since it would require more than 9 digits to create.

def checkPandigital(a, b):
    check = list()
    for digit in str(a):
        check.append(int(digit))
    for digit in str(b):
        check.append(int(digit))
    for digit in str(a*b):
        check.append(int(digit))
    if sorted(check) == sorted(range(1,10)):
        return True
    else:
        return False

solutionSet = set()
for a in range(1, 100):
    for b in range(100, 10000):
        if checkPandigital(a, b):
            solutionSet.add(a*b)

print(solutionSet)
print(f"There are {len(solutionSet)} pandigital products. Their sum is {sum(solutionSet)}")