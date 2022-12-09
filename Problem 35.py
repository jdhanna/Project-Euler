# Problem 35: https://projecteuler.net/problem=35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# Solution: Four step process:
# 1) Generate all the primes under 1 million. (Thanks again problem 3)
# 2) Then write a function that generates all rotations.
# 3) Then check all the rotations.
# 4) Aggregate Results

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
primes = sieve(limit)

def generateRotations(n):
    def rotate(a): #Pass this function a string, and it will return a rotated string.
        return a[-1] + a[0:len(a)-1]

    solutions = set()
    solutions.add(int(n))
    test = str(n)
    while True:
        test = int(rotate(str(test)))
        if test in solutions:
            return solutions
        else:
            solutions.add(test)

answers = set()
answers.add(2)
answers.add(3)
answers.add(5)
answers.add(7)
# We add the 1 digit cases, because our "rotate" function will throw an error on one digit inputs.

for i in range(10, limit):
    if i in primes:
        trial = generateRotations(i)
        withPrimes = trial.intersection(primes)
        if withPrimes == trial:
            answers.add(i)

print(f"There are {len(answers)} circular primes below {limit}")
