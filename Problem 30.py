# Problem 30: https://projecteuler.net/problem=30

# There are only 3 numbers that can be written as the sum of 4th powers of their digits. (Excluding 1^4 = 1 as it is not a sum)
# Find the sum of all numbers that can be written as the sum of fifth powers of their digits.

# Solution: The tricky part here is to know when to stop testing. a 7 digit number will number have a digital 5th-power sum that is 7 digits.
# This trend will continue on higher orders of magnitude.

def digitSum(num, power):
    ans = 0
    for a in str(num):
        ans += int(a)**power
    return ans

def seek(power, limit):
    i = 9
    ans = 0
    while i < limit:
        i+=1
        test = digitSum(i, power)
        if test == i:
            print(f"{i} has a {power}th power digital sum of {test}")
            ans += i
    print(f"The sum of all positive integers whose {power}th power digital sum is themselves is {ans}")

seek(4, 1000000)
seek(5, 6*(9**5) + 1)


