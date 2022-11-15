# Problem 16: 2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26
# What is the sum of the digits of the number 2^1000

# Solution: Python handles all the dirty work here. Write a function to find the digital sum of a number and Python will pass 2^1000 just fine.

def digitalSum(n):
    a = [int(x) for x in str(n)]
    return sum(a)

print(digitalSum(2**15))
print(digitalSum(2**1000))