# Problem 39: https://projecteuler.net/problem=39

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

# Solution: We'll generate all pythagorean triples where no side length is above 500 (which will guarantee we find all the perimeters less than 1000 by the triangle inequality) then we'll sort them into buckets by perimeter.

# There are several algorithms to find all the pythagorean triples up to a certain size, but these are small enough that we can find them by brute force to keep things simple

# We'll be performing the "Square" operation lots, so it's quicker to store them in memory.
limit = 501
squares = [i*i for i in range(limit)]

triples = set()
for a in range(1, limit):
    for b in range(a, limit):
        cSquare = squares[a] + squares[b]
        if cSquare in squares:
            triples.add((a, b, int((cSquare)**0.5)))

resultSet = [0 for p in range(2000)]
for triple in triples:
    p = sum(triple)
    resultSet[p] += 1

m = max(resultSet)
ans = resultSet.index(m)

print(f"The perimeter with the most triples under 1000 is {ans} with {m} triples")

