# Problem 33: https://projecteuler.net/problem=33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def doesCancel(a, b):
    aFirst = int(str(a)[0])
    aLast = int(str(a)[1])
    bFirst = int(str(b)[0])
    bLast = int(str(b)[1])

    if bLast == 0 or aLast == 0:
        return False
    if aFirst == bFirst or aLast == bLast:
        return False # This is just a trivial example.
    if aFirst == bLast: # Check if digits even cancel at all.
        if aLast/bFirst == a/b: # Check if they cancel in this misleading way
            return True
        else:
            return False
    elif aLast == bFirst: # Check if digits even cancel at all.
        if aFirst/bLast == a/b: # Check if they cancel in this misleading way
            return True
        else:
            return False
    return False

solution = set()
for a in range(10,100):
    for b in range(a, 100):
        if doesCancel(a,b):
            solution.add((a,b))

print(f"There are {len(solution)} 2-digit digit-cancelling fractions. They are as follows:")
for item in solution:
    print(f"{item[0]}/{item[1]}")
print('')

# We'll factor this in lowest terms. We know the factors all have to be less than 100, so we can just multiply and check with brute force.
# This process is a little cumbersome, but not too bad. It could be avoided by importing the "fractions" package in python.

num = 1
den = 1
for item in solution:
    num *= item[0]
    den *= item[1]

print(f"The product of these factors is {num}/{den}")

factor = 2
while factor <100:
    if num%factor == 0 and den%factor == 0:
        num = int(num/factor)
        den = int(den/factor)
    else:
        factor += 1

print(f"In lowest terms this is {num}/{den}")
