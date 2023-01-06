# Problem 31: https://projecteuler.net/problem=31

# In the UK (as of 2022) the currency is made up of the pound and the pence. There are 8 coins in circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

# How many ways can you make 200p using any number of coins?

# Solution: Rather than using some generating function, this is a good target for dynamic programing.

from time import time

stime = time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Initialize our solution.
# This change vector is going to represent the number of ways
# to make the target value with only the coins allowed so far.

change = [0 for x in range(0, 201)]
change[0] = 1  # There's one way to make no money with no coins.

for coin in coins:
    # We'll start by building the answer to the question
    # "How many ways can you make change with a penny",
    # then adding in coins one by one.
    for i in range(coin, 201):
        change[i] = change[i - coin] + change[i]  # The critical step.

etime = time()
diff = 1000 * (etime - stime)

print(f"There are {change[200]} ways to make change for 2 pounds with British coins.")
print(f"Elapsed time = {diff} milliseconds")
