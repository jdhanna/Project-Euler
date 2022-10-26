# Problem Statement:
# The sum of the squares of the first ten natural numbers is 385.
# The square of the sum of the first ten natural numbers is 3025.
# The difference between the two is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Solution:
# It isn't particularly computationally intensive, but there are explicit formulas that can be used to calculate each of these.

def squareSum(n):
    #Find the square of the sum of the first n natural numbers

    # There's an explicit formula to find the sum of the first n natural numbers. Pair the first number with the last, the second number with the second to last. etc...
    # Each pair has the same value. So multiply that value (n+1) by the number of pairs (n/2)
    answer = (n*(n+1)/2)**2
    return int(answer)

def sumSquares(n):
    #Find the sum of the squares of the first n natural numbers

    #The derivation for this formula is less nice, but it simplifies well:

    answer = (n*(n+1)*((2*n)+1)/6)
    return int(answer)

def main(n):
    print(squareSum(n) - sumSquares(n))
    return

main(10) # Confirm that this is indeed 2640
main(100)