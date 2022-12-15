# Problem 47: https://projecteuler.net/problem=47
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of those numbers?

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

def numFactors(number, primes):
    ans = 0
    i = 0
    prime = primes[i]
    while prime <= number:
        if number%prime == 0:
            ans += 1
        i += 1
        prime = primes[i]
    return ans

limit = 1000000
primes = sorted(list(sieve(limit)))

n = 5 # We'll start at 5 to avoid n = 1 issues.
a = 1 # a will be the number of factors n has
b = 1 # b will be the number of factors n-1 has
c = 1 # c will be the number of factors n-2 has
d = 1 # d will be the number of factors n-3 has
factors = (a, b, c, d)
while factors != (4, 4, 4, 4):
    n += 1
    d = factors[2]
    c = factors[1]
    b = factors[0]
    a = numFactors(n, primes)
    factors = (a,b,c,d)
    #print(f"{n} has {a} factors")

print(f"The first four consecutive integers with 4 distinct prime factors is {n-3}, {n-2}, {n-1}, and {n}")