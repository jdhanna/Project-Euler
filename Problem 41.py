# Problem 41: https://projecteuler.net/problem=41

# What is the largest n-digit pandigital prime that exists?

# Solution: We can brute force ourselves a solution fairly easily here with the prime generator from problem 3 and the pandigital checker from problem 38.
# We can improve performance by wisely choosing our limit, and checking in reverse order.

limit = 8000000 # No prime can be 9-digit pandigital since it fails the "divide by 3" test (1+2+3+4+5+6+7+8+9 = 45 which is divisible by 3).
# Similarly no prime can be 8 digit pandigital since it also fails the "divide by 3 test (1+2+3+4+5+6+7+8 = 36 which is divisible by 3).
# We can limit it even a little further by not bothering to check primes starting with an 8.

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

primes = sorted(list(sieve(limit)), reverse=True)
print("Generated Primes.")
print("")

def isPandigital(n):
    digits = sorted([int(a) for a in str(n)])
    test = [i for i in range(1,len(str(n))+1)]
    return digits == test

for number in primes:
    if isPandigital(number):
        print(f"The largest {len(str(number))}-digit pandigital prime is {number}")
        break







