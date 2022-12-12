# Problem 36: https://projecteuler.net/problem=36

#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

# Solution: This is straightforward.

# 1) Write a function converting the number to a binary string
# 2) Write a function checking to see if a given string is a palindrome
# 3) Run this function across every every integer less than one million.

limit = 1000000

def toBinary(n):
    return str(bin(n))[2:]

def isPalindrome(s):
    return s == s[::-1]

ans = 0
for num in range(limit):
    if isPalindrome(str(num)):
        if isPalindrome(str(toBinary(num))):
            ans += num

print(f"The sum of all numbers less than {limit} which are palindromic in base 10 and base 2 is {ans}")
