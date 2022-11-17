# Problem 25: How many steps do you need to go out to reach the first 1000 digit Fibonacci number:

# Solution: Again python's smart handling of long ints to the rescue here.

def findFibSize(limit):
    ans = 1
    old = 0
    new = 1
    while len(str(new)) < limit:
        c = old + new
        old = new
        new = c
        ans += 1

    return ans

#print(findFibSize(3)) # Confirm this is 12
print(f"The first Fibonacci number to contain 1000 digits is the {findFibSize(1000)}th Fibonacci number")
