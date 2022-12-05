# Problem: For what value of d < 1000 does 1/d contain the longest recurring cycle in its decimal fraction part

# Solution: We'll manually perform the long division until we get to a remainder that is a repeat of what we've already seen. Then we'll count that distance.

def cycleLen(d):
    start = 1
    usedRemainders = list()
    while True:
        remainder = start % d
        start = 10 * remainder
        if remainder in usedRemainders:
            break
        else:
            usedRemainders.append(remainder)

    if remainder == 0:
        return 0 # While the 0s do technically repeat forever, creating a cycle of 1, it's useful for testing purposes to see if we're correctly identifying digits that evenly divide.
    else:
        return len(usedRemainders) - usedRemainders.index(remainder)

'''
#Test if cycleLen() is working properly
def testCycleLen(d):
    print(f"1/{d} has a cycle of {cycleLen(d)}")
    return

for i in range(2, 100):
    testCycleLen(i)
'''
limit = 1000
best = 1
for i in range(2, limit):
    test = cycleLen(i)
    if test > best:
        best = test
        d = i

print(f"The longest cycle under {limit} occurs at d={d} with a cycle of {best}")
