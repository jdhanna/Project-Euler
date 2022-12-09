# Problem 34: https://projecteuler.net/problem=34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Solution: The tricky part here is knowing when to stop. 9! is 362880. 9 of those digits would only be 7 digits long, so we'll stop when we get to 7 digits.


# Since we'll be calling factorial many times, it's better to just calculate the factorial for each digit once and store to memory.
fact =[1, 1]
for i in range(2, 10):
    fact.append(fact[-1]*i)

def factSum(n, fact):
    ans = 0
    for digit in str(n):
        ans += fact[int(digit)]
    return ans

solutions = set()
for target in range(10, 10000000):
    if factSum(target, fact) == target:
        solutions.add(target)

print(f"The only solutions are {solutions}, their sum is {sum(solutions)}")