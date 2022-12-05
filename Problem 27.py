# Problem 27: n^2 + n + 41 will produce prime numbers for values of n between 0 and 39. For what values a and b (both between -1000 and 1000) does n^2 + an + b produce the most primes starting at n = 0

# Solution: Most of the effort here goes into searching carefully and quickly. The solution itself is fairly straightforward:
# --We generate a large enough list of primes (again re-using work from problem 3).
# --Then we make function that tests how long a given quadratic will produce primes
# --Then select the largest.

# We'll never need to check if a number is prime larger than 2,001,000 as the problem limits us to considerations of a and b < 1000

limit = 2001000

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

# Furthermore, since the problem specifies we start at n = 0, each function will evaluate to f(n) = b at n = 0.
# Thus, if b is not a positive prime, we don't need to check it.
possibleB = sorted(list(sieve(1000)))

def checkQuadratic(a,b, primes):
    # This function will check how long a given quadratic will generate primes starting at n=0
    def f(n):
        return (n*n) + (a*n) + b

    i = 0
    while f(i) in primes:
        i += 1
    return i

# Some quick tests to ensure our checkQuadratic Function is working properly.
#print(checkQuadratic(1, 41, primes))
#print(checkQuadratic(-79, 1601, primes))

best = 1
for a in range(-1000, 1000):
    for b in possibleB:
        test = checkQuadratic(a, b, primes)
        #print(f"a is {a}, b is {b}, test is {test}")
        if test > best:
            best = test
            ansA = a
            ansB = b

print(f"The quadratic that produces the maximum number of primes for consecutive values of n, starting with n=0 is n^2 + {ansA}n + {ansB}, producing {best} primes.")
print(f"The best a is {ansA}, the best b is {ansB} and the product is {ansA*ansB}")

