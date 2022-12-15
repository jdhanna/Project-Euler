# Problem 48: https://projecteuler.net/problem=48

# What are the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000

# Solution: The solution is straightforward. Just be careful to apply "last10" at each step to avoid issues with very large integers.

def last10(num):
    return int(str(num)[-10:])

limit = 1000
series = [last10(x**x) for x in range(1, limit+1)]

print(f"The last ten digits of the series in question are {last10(sum(series))}")
