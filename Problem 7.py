# Problem Statement:
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

# Solution:
#We can start by using the same code from Problem 3 to generate a list of primes.

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

# We have a function that will generate primes up to a specific target. We just need to make sure that list of primes is big enough.

# The prime counting function [pi of x] counts the number of primes below x.
# As best we can tell, pi of x grows at about a rate of x/ln(x).
# Using this formula, we can find a rough estimate to start our search: 10,001 = x/ln(x) implies that x is about 116684 (thanks to wolfram alpha).
# Starting 2x this figure should give us plenty of room to find teh 10,001st prime.

print(sorted(list(sieve(2*116684)))[10000])


