# Problem 44: https://projecteuler.net/problem=44

#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

# Solution: There are not many pentagonal numbers that sum and subtract to other pentagonal numbers. Brute force is too slow to work here.
# Instead, we can make use of a nice property of the pentagonal numbers. You can quickly test if a number is pentagonal by evaluating if sqrt(24x + 1) + 1 == 5 mod 6.

limit = 10000
pentagonals = list()
print("Pentagonal Numbers Generated")

def testPent(num):
    return (((24*num)+1)**0.5)%6 == 5

def mPent(num):
    return int(n*((3*n)-1)/2)

n = 1
new = mPent(n)
pentagonals.append(new)
solutions = set()
while n < limit:
    n += 1
    new = mPent(n)
    for pent in pentagonals:
        if testPent(pent + new) and testPent(new-pent):
            solutions.add((pent, new))
            break
    pentagonals.append(new)

best = mPent(limit)
for item in solutions:
    s = item[0] + item[1]
    d = item[1] - item[0]
    if d < best:
        best = d
        top = item[1]
        bottom = item[0]

print(f"The best pair of pentagonal numbers with this property is {bottom} and {top}. Their difference is {best}")


