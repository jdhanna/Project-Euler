# Problem 43: https://projecteuler.net/problem=43

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17

#Find the sum of all 0 to 9 pandigital numbers with this property.

# Solution, we'll generate all the 0-9 pandigitals, (by generating all permuations of 0,1,2,3,4,5,6,7,8,9 and check them manually

from itertools import permutations

perms = [''.join(p) for p in permutations('0123456789')]
pandigitals = set()
for item in perms:
    if item[0] != '0':
        pandigitals.add(item)

def checkProperty(s):
    a = s[1]+s[2]+s[3]
    b = s[2]+s[3]+s[4]
    c = s[3]+s[4]+s[5]
    d = s[4]+s[5]+s[6]
    e = s[5]+s[6]+s[7]
    f = s[6]+s[7]+s[8]
    g = s[7]+s[8]+s[9]
    if int(a)%2 == 0 and int(b)%3==0 and int(c)%5 == 0 and int(d)%7==0 and int(e)%11==0 and int(f)%13 == 0 and int(g)%17==0:
        return True
    else:
        return False

# print(checkProperty("1406357289")) #Test if this is true

solution = set()
for item in pandigitals:
    if checkProperty(item):
        solution.add(int(item))

print(f"There are {len(solution)} pandigitals with this property, and they are {solution}, they sum to {sum(solution)}")

