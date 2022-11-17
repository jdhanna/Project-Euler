#Problem 23: An "Abundant Number" is a number which is smaller than the sum of its proper divisors. I.E. 12 < 1 + 2 + 3 + 4 + 6 = 16

# All integers greater than 28123 can be written as the sum of two abundant numbers.

# Find the sum of all positive integers which *cannot* be written as the sum of two abundant numbers.

# Solution: We'll find all abundant numbers less than the limit of 28123, and then this problem reduces to an iterated "twosum" problem.

def isAbundant(n):
    ans = 0
    for i in range(1, int((n/2))+1):
        if n%i == 0:
            ans += i
    if ans > n:
        return True
    else:
        return False

def findAbundant(limit):
    # A brute force approach to finding abundant numbers is fine here since the limit is small.
    ans = list()
    for i in range(11, limit): # The first abundant number is 12
        if isAbundant(i):
            ans.append(i)
    return ans

def twoSum(target, array):
    partners = set() # Traditionally you use a dictionary, but we don't actually need to know the pair, we just need true/false on if such a pair exists.
    for item in array:
        if item in partners or item*2 == target:
            return True
        else:
            partners.add(target-item)
    return False

def main():
    abundantNumbers = findAbundant(28123)
    print("Abundant Numbers Found")
    ans = 0
    ansList = list()
    for i in range(0,28124):
        if not twoSum(i, abundantNumbers):
            ansList.append(i)
            ans += i
    print(ansList)
    print(f"The sum of all positive integers that cannot be made from two abundant numbers is {ans}")
    return

main()