import time

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def rank(hits):
    return int((hits+3)/2)

def laserBeam(hits):
    a = time.time()
    row = rank(hits)
    ans = 0
    offset = 3-row%3

    for i in range(offset, row, 3):
        if gcd(row, i) ==1:
            ans += 1
    print("Time Taken was: " + str(round(time.time()-a,2)))
    return ans

print(laserBeam(11))
print(laserBeam(1000001))
print(laserBeam(12017639147))

#print(laserBeamSpec())



'''
def laserBeamSpec():
    hits = 12017639147
    #For this particularly large number, the for loop will take forever.
    #I factored rank(12017639147) in advance, but any factoring method you use will work
    factors = [5 , 11 , 17 , 23 , 29 , 41 , 47]
    row = rank(hits)
    ans = 0
    offset = 3-row%3

    for i in range(offset, row, 3):
        for p in factors:
            if i%p != 0:
                ans += 1
    return ans

def laserBeam2(m):
    # laserBeam1 will work if m is small enough, but if m is very large, we need to speed up the process.
    # this means laserBeam2 will undergo the unfortunate process of factoring m
    n = int(m ** 0.5) + 1
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = list()
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    factors = list()
    row = int(rank(m))
    for p in primes:
        if row % p == 0:
            factors.append(p)
            row = row / p
    ans = 0
    offset = int(3-(row%3))

    for i in range(offset, row, 3):
        for p in factors:
            if i%p != 0:
                ans += 1
    print(ans)
    return

laserBeam2(1000001)
'''