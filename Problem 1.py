def findSumA(n):
    ans = 0
    for i in range(0,n):
        if i%3 == 0 or i%5==0:
            ans += i
    return ans

def findSum(n,fact):
    if n%fact == 0:
        size = int(n/fact)-1
    else:
        size = int(n/fact)
    return fact*size*(size + 1)/2

def findSumB(n):
    return findSum(n, 3) + findSum(n, 5) - findSum(n, 15)

print(findSumB(1000))