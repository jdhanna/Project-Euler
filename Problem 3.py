# Problem Statement:

# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of 600851475143?

# Solution
# We need to generate some prime numbers first. One "quick" way to do this is use the sieve of erastosthenes.

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

# Now that we have a function that can generate all the potential primes, let's cycle through them and find the prime factors.

def primeFactors(n):
    primes = sieve(int(n**0.5) + 1)
    ans = set()
    for p in primes:
        if n%p == 0:
            ans.add(p)
    return ans

# Now that we have the distinct prime factors, lets grab the largest.

def largestPrimeFactor(n):
    return max(primeFactors(n))

# Let's confirm everything is working properly by checking the example problem. 13195 should return 29
print(largestPrimeFactor(13195))

# With that out of the way, we'll run this for the actual problem.
print(largestPrimeFactor(600851475143))