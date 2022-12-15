# Problem 50: https://projecteuler.net/problem=50

# Which prime below one-million can be written as the sum of the most consecutive primes?

# Solution: We take a brute force solution of generating all the primes under a million and testing all the series that can be made.
# My solution is slower than I'd like, but still runs in about a minute, which is the cutoff for success.

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

limit = 1000000
primes = sorted(list(sieve(limit)))

best = 20
for i in range(len(primes) - 1):
    series = primes[i]
    j = i+1
    while series < limit:
        series += primes[j]
        if series in primes:
            bestJ = j
        j += 1
    test = bestJ-i
    if test > best:
        best = test
        bestI = i
        bestEnd = bestJ

ans = 0
for i in range(bestI, bestEnd+1):
    ans += primes[i]

print(f"The longest streak of primes is {best} long. It starts at {primes[bestI]} and ends at {primes[bestEnd]} and sums to {ans}")








