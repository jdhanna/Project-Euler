# Problem 49: https://projecteuler.net/problem=49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# Solution: No trick here to be had. Just leverage work done from earlier problems in prime numbers and permutations.

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

limit = 10000
bPrimes = sieve(limit)
primes = list()
for i in range(1000, 9999): # This step does the sorting and filtering for us in one loop.
    if i in bPrimes:
        primes.append(i)

def arePermutations(a,b):
    return sorted(str(a)) == sorted(str(b))

solution = set()
for i in range(len(primes)-1):
    for j in range(i+1, len(primes)):
        if arePermutations(primes[i], primes[j]):
            d = primes[j] - primes[i]
            new = d + primes[j]
            if new in primes:
                if arePermutations(new,primes[j]):
                    solution.add((primes[i], primes[j], new))

print(f"The two solutions are {solution}")


