# Problem Statement:
# What is the value of the first triangle number to have over five hundred divisors?

# Solution:
# We'll use brute force here--generate each triangular number and check its number of divisors.

def numDivisors(n, primes):
    # The brute force method for determining the number of factors is somewhat barbaric here.
    # A better way is to find the prime factorization of the number in question.
    # Then a simple combinatorics exercise finds the number of total factors

    factorization = list()
    primes = sorted(list(primes))
    i=0
    a = n
    if n in primes:
        factorization.append(n)
    else:
        while primes[i] < (n/2) +1:
            if a%primes[i] == 0:
                factorization.append(primes[i])
                a = a/primes[i]
            else:
                if i+1 > len(primes):
                    print("Error: List of prime numbers not large enough")
                    break
                i = i+1
    answer = 1
    for prime in set(factorization):
        answer = answer * (1+factorization.count(prime))
    return answer


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


def search(limit):
    primes = sieve(10000) # It's important to limit this as searching a big list of prime numbers is the costly part of the algorithm.
    numFactors = dict()
    numFactors[1] = 1
    numFactors[2] = 2
    numFactors[3] = 2
    n = 3
    while True:
        num = int(n*(n+1)/2)
        numFactors[n+1] = numDivisors(n+1,primes)
        if n%2 == 0:
            a = numFactors[n+1]
            b = numFactors[n/2]
            attempt = int(a*b)
        else:
            a = numFactors[(n+1)/2]
            b = numFactors[n]
            attempt = int(a*b)
        if attempt >= limit:
            print(f"n={n}: {num} has passed with {a} * {b} = {attempt} factors")
            break
        else:
            n += 1
            print(f"n={n-1}: {num} has failed with {a} * {b} = {attempt} factors")
    return

search(5)
search(500)