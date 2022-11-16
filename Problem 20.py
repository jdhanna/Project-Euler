# Problem 20: The digital sum of 10! is 27. What is the digital sum of 100!

# Solution: This is another one that python can straightforwardly handle thanks to its proper handling of long integers.

import math

def digitalSum(n):
    return sum([int(x) for x in str(n)])

print(digitalSum(math.factorial(10))) # Verify this is 27
print(digitalSum(math.factorial(100)))