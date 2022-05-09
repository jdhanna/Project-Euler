
# Problem Statement:  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

#Solution: This is the classic "Fizzbuzz" problem. I've put together 2 solutions.

#Find Sum A is just a simple solution to FizzBuzz
def findSumA(n):
    ans = 0
    for i in range(0,n):
        if i%3 == 0 or i%5==0:
            ans += i
    return ans


#Find Sum B is trying to be a little quicker about things. All the numbers with a factor of 3 form a geometric series. If we add the geometric series for 3, 5, and subtract the one from 15, we'll end with the right figure without actually looping all the way through.
def findSum(n,fact):
    if n%fact == 0:
        size = int(n/fact)-1
    else:
        size = int(n/fact)
    return fact*size*(size + 1)/2

def findSumB(n):
    return int(findSum(n, 3) + findSum(n, 5) - findSum(n, 15))

print(findSumB(1000))