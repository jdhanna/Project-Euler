# Problem 38: https://projecteuler.net/problem=38

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Solution: We'll generate each concatenated product under a certain size, filter out the ones that aren't 9 digits, and filter out the ones that aren't pandigital, then select the largest

def concatenatedProduct(number, n):
    s = str()
    for i in range(1, n+1):
        s = s + str(i*number)
    return s

# Test the concatenatedProduct() function:
# print(concatenatedProduct(192, 3))

def isPandigital(n):
    test = [int(a) for a in str(n)]
    test = sorted(test)
    return test == [1,2,3,4,5,6,7,8,9]


best = 0
for n in range(2, 5): #5 is the upper bound here for a single digit case
    for num in range(1,10000): #10000 is the upper bound here since n must be greater than 2.
        target = int(concatenatedProduct(num, n))
        if isPandigital(target):
            if target>best:
                best = target
                bestNum = num
                bestN = n

print(f"The largest 1 to 9 pandigital that can be formed as a concatenated product is {best} which is made from {bestNum} and {range(1,bestN)}")

