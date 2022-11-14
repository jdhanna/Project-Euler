# Problem Statement:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Solution:
# Math can do the heavy lifting here:
# Take a lattice point on the first quadrant of the complex plane and square it.
# Because we started with a lattice point and we're performing multiplication and addition, we'll end on a lattice point.
# However, because complex squares can also be modeled by a linear transformation on the plane (a rotation and a stretch), the distance to the origin will also be an integer.

# Some of these triples will be degenerate (8,0,8) is not a very useful triple.
# But the ease of computation here is worth the trade off of generating a few extra degenerate solutions.

# (u+vi)*(u+vi) = u^2 - v^2 + 2uvi
# (u^2 - v^2, 2uv, u^2 + v^2) will be our triple.


triples = set()
for u in range(1,33):
    for v in range(1,u):
        triples.add((u**2 - v**2, 2*u*v, u**2 + v**2))

for triple in triples:
    if triple[0] + triple[1] + triple[2] == 1000:
        print(triple)
        print(triple[0]*triple[1]*triple[2])

