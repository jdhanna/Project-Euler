# Problem Statement: Find the sum of all the primes below two million.

# Solution:
# This is a straightforward application of the work from problem 3.

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

def sumPrimes(n):
    return sum(sieve(n))

print(sumPrimes(10)) # Verify that this is 17 as the example suggests
print(sumPrimes(2000000))

