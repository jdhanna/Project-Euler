# Problem 40: https://projecteuler.net/problem=40

#An irrational decimal fraction is created by concatenating the positive integers:
#0.12345678910*1*112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

#Solution: We'll write out champernowne's constant and perform the multiplication. If this were a larger problem we wouldn't want to commit the entire thing to memory, but those contraints aren't serious here.

champernowne = list()
champernowne.append(0) #Thus champernowne[n] will always return the nth digit of champernowne's constant

limit = 1000001
i = 1
while len(champernowne) < limit:
    s = str(i)
    for digit in s:
        champernowne.append(int(digit))
    i += 1

# print(champernowne[12]) # Confirm that this is 1.

answer = champernowne[1] * champernowne[10] * champernowne[100] * champernowne[1000] * champernowne[10000] * champernowne[100000] * champernowne[1000000]

print(f"The expression resolves to {champernowne[1]} x {champernowne[10]} x {champernowne[100]} x {champernowne[1000]} x {champernowne[10000]} x {champernowne[100000]} x {champernowne[1000000]} which equals {answer}")
