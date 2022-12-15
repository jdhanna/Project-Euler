# Problem 46: https://projecteuler.net/problem=46

# It was also propsed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square. This conjecture is false.
# What is the smallest counterexample?

# Solution:

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
odds = [(2*x)+1 for x in range(int(limit/2))]
oddComposites = list()
for number in odds:
    if number not in primes:
        oddComposites.append(number)

solvable = set(oddComposites)

for item in primes:
    i = 1
    s = item
    while s < limit:
        s = 2*i*i + item
        solvable.discard(s)
        i += 1

print(f"The only odd composites I could not produce from a prime and twice a square were {solvable}")





