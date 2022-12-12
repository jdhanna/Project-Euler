# Problem 37: https://projecteuler.net/problem=37

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Solution: It's challenging to know what limit to set, especially given the fact that generating primes is expensive.
# We'll generate a small number (all primes under 1 million at first) and check from there.

limit = 1000000

def sieve(limit):
    primes = [True for i in range(limit+1)]
    primes[0] = False
    primes[1] = False
    j = 2
    while j*j <= limit:
        if primes[j]:
            for i in range(j*j, limit + 1, j):
                primes[i] = False
        j += 1

    actualPrimes = set()

    for i in range(len(primes)):
        if primes[i]:
            actualPrimes.add(i)

    return actualPrimes

primes = sieve(limit)

def truncLtoR(n):
    a = str(n)
    response = set()
    for i in range(len(a)):
        response.add(int(a[i:]))
    return response

def truncRtoL(n):
    a = str(n)
    response = set()
    for i in range(1, len(a)):
        response.add(int(a[0:i]))
    return response # This loses n itself, which is a feature, we don't want to be checking it twice.

solution = set()
for prime in primes:
    x = truncRtoL(prime)
    y = truncLtoR(prime)
    z = x.union(y)
    if z == z.intersection(primes):
        solution.add(prime)

solution.remove(2)
solution.remove(3)
solution.remove(5)
solution.remove(7)

print(f"There are {len(solution)} perfectly truncatable primes, they are {solution}. Their sum is {sum(solution)}")


