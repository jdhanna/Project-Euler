# Problem 45: https://projecteuler.net/problem=45

# Find the 2nd triangular number that is also pentagonal and hexagonal

# Solution: As discussed in Problem 44, there's an easy test for pentagonal numbers. There's a similar test for hexagonal numbers.

def testPent(num):
    return (((24*num)+1)**0.5)%6 == 5

def testHex(num):
    return (((8*num)+1)**0.5)%4 == 3

def genTri(num):
    return int(num*(num+1)/2)

solutions = list()
n = 1
while len(solutions) < 2:
    n += 1
    a = genTri(n)
    if testPent(a) and testHex(a):
        solutions.append(a)

print(f"The 2nd triagonal number that is also hexagonal and pentagonal is {solutions[1]}")