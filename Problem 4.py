# Question: Find the largest palindrome made from the product of two 3-digit numbers.

# Solution: This is pretty simple. Multiply all the 3 digit numbers by each other and find the largest that happen to be a palindrome.


# Write a function determining if a number is a plaindrome.
def isPalindrome(n):
    return str(n) == str(n)[::-1]

# We can generate all the 3-digit products relatively quickly, but we can speed things up by cutting off our calculation if all our remaining products will be smaller than a palindrome we've already found.

def checkProduct(top, bot):
    best = 0
    for a in range(top, bot, -1):
        if a*(a-1) < best:
            break

        for b in range(a, bot, -1):
            current = a*b
            if isPalindrome(current):
                if current > best:
                    best = current

    return best

print(checkProduct(999, 99))





