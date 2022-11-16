# Problem 21:  Find the sum of all amicable numbers under 10000

# Solution: Since the problem only asks us for the numbers under 10000, brute force is plenty fast enough for a solution.

def findSumDivisors(n):
    ans = 0
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            ans += i
    return ans

def findAmicableSum(limit):
    amicable = dict()
    for i in range(1, limit + 1):
        if findSumDivisors(i) > limit:
            amicable[i] = -1
        else:
            amicable[i] = findSumDivisors(i)
    amicable[0] = -1
    amicable[-1] = -1

    ans = 0

    for i in range(1, limit + 1):
        if i == amicable[amicable[i]] and i != amicable[i]:
            ans += i


    print(ans)
    return


findAmicableSum(10000)

