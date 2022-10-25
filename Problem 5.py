# Problem Statement:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This question essentially asks for the Least Common Multiple of the integers between 1 and 20. We could naively search integers testing if each one is evenly divisible by 1 through 20 in the worst fizzbuzz of all time, but there's a faster method.

# First, we'll reuse the code from Problem 3 to generate a list of prime numbers.

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

def prod(nums):
    answer = 1
    for i in nums:
        answer *= i
    return answer




def largeLCM(n):
    #Generate all the primes. Each copy will have to be in the answer.
    primes = sieve(n)

    # We also need the largest power of each prime factor that would still be less than n.
    factors = list()
    for item in primes:
        a = item
        while a <= n:
            a *= item
        factors.append(a/item)

    answer = int(prod(factors))
    return answer


print(largeLCM(10)) # Confirm this is equal to 2520 as given in the problem
print(largeLCM(20))
