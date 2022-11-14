# Problem: Take a number n. If n is odd, replace it with 3n+1. If n is even, replace it with n/2. As you repeat this process, it is hypothesized that all starting values collapse to n = 1
# What starting value under 1 million produces the longest chain

# Solution: A brute force solution is simple enough, but we can save a lot of time by reusing results we've already found.

# The key of the dictionary will mark the number of steps needed to reach 1.

collatz = dict()
collatz[1] = 0
collatz[2] = 1
limit = 1000000

def assignValue(n, collatz):
    if n%2 == 0:
        newN = int(n/2)
    else:
        newN = (3*n) + 1

    while True:
        try:
            collatz[n] = collatz[newN] + 1
        except KeyError:
            assignValue(newN, collatz)
            continue
        break

    return

for i in range(1,limit):
    assignValue(i, collatz)

ans = 13
for i in range(1,limit):
    if collatz[i] > collatz[ans]:
        ans = i

print(f'The longest chain with starting number under {limit} starts with {ans} and proceeds {collatz[ans]+1} steps.')
#print(collatz)


