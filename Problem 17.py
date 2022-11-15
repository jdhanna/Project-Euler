# Problem: If the numbers 1 to 5 were written out in words, then there are 19 total letters used.
# If all the numbers from 1 to 1000 were written out in words, how many letters would be used? (Not counting hyphens or spaces)

# Solution: The challenge here is writing a function that properly converts integers to English.

def stripSpaces(s):
    # This function strips out the spaces in a given string.
    if s is None:
        return ""
    else:
        return s.replace(" ", "")

def createWord(n):
    def oneDigit(n):
        if n == 0: # If twoDigit receives a number ending in 0, we want one Digit to just return the tens base.
            return ""
        elif n == 1:
            return "One"
        elif n==2:
            return "Two"
        elif n==3:
            return "Three"
        elif n==4:
            return "Four"
        elif n==5:
            return "Five"
        elif n==6:
            return "Six"
        elif n==7:
            return "Seven"
        elif n==8:
            return "Eight"
        elif n==9:
            return "Nine"
        else:
            print(f"Error: {n} This is not a one digit integer")

    def twoDigit(n):
        if n < 10:
            return oneDigit(n)
        elif n >= 90:
            return "Ninety" + oneDigit(n-90)
        elif n >= 80:
            return "Eighty" + oneDigit(n-80)
        elif n >= 70:
            return "Seventy" + oneDigit(n-70)
        elif n >= 60:
            return "Sixty" + oneDigit(n-60)
        elif n >= 50:
            return "Fifty" + oneDigit(n-50)
        elif n >= 40:
            return "Forty" + oneDigit(n-40)
        elif n >= 30:
            return "Thirty" + oneDigit(n-30)
        elif n >= 20:
            return "Twenty" + oneDigit(n-20)

        if n == 10:
            return "Ten"
        elif n == 11:
            return "Eleven"
        elif n == 12:
            return "Twelve"
        elif n == 13:
            return "Thirteen"
        elif n == 14:
            return "Fourteen"
        elif n == 15:
            return "Fifteen"
        elif n == 16 or n == 17 or n == 19:
            return oneDigit(n-10)+"teen"
        elif n == 18:
            return "Eighteen"

        return

    def threeDigit(n):
        if n == 1000:
            return "One Thousand"
        a = int(str(n)[0]) # The first digit
        b = int(str(n)[1:]) # The second two digits
        if b != 0:
            return oneDigit(a) + "Hundred and" + twoDigit(b)
        else:
            return oneDigit(a) + "Hundred"

    if n > 99:
        return stripSpaces(threeDigit(n))
    elif n > 9:
        return stripSpaces(twoDigit(n))
    else:
        return oneDigit(n)

def letterCount(n):
    ans = 0
    for i in range(1, n+1):
        ans += len(createWord(i))
        print(f"{i}: {createWord(i)} has {len(createWord(i))} characters")
    return ans

print(letterCount(5)) # Confirm this is 19.
print(letterCount(1000))

