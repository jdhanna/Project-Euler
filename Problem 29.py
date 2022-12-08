# Problem 29: https://projecteuler.net/problem=29

# How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

# Solution: Python's "set" data structure will ensure we don't allow duplicates.

def sequenceLength(aMax, bMax):
    sequence = set()
    for a in range(2, aMax+1):
        for b in range(2, bMax+1):
            sequence.add(a**b)
    return len(sequence)

print(f"The test sequence has a length of {sequenceLength(5, 5)}")
print(f"The problem sequence has a length of {sequenceLength(100, 100)}")