# Problem 42: https://projecteuler.net/problem=42

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# How many triangle words are found in the file p042_words.txt ?

# Solution: We'll reuse the work from Problem 22 to make the file into a python list. Then we'll generate all the triangle numbers, and see if each scored word falls in the triangle set.

def readFile(path):
    with open(path) as f:
        rawText = f.readlines()
        rawText = rawText[0]
    return rawText

def stringToList(rawText):
    names = list()
    a=0
    b=1
    while b != -1: # Some care is needed here to strip out the quotes and commas, and not incorrectly cut off the last name.
        c = rawText[a+1:].find('"')
        nextName = rawText[a+1:a+c+1]
        names.append(nextName)
        b=rawText[a:].find(',')
        a = a + b + 1
    return names

def score(s):
    ans = 0
    for letter in s:
        ans += ord(letter)-64
    return ans

rawText = readFile('Data/p042_words.txt')
wordList = stringToList(rawText)

triangles = list()
triangles.append(0)
# The triangular numbers can be given by that formula, but they can also be found recursively
for i in range(1, 101):
    triangles.append(i+triangles[i-1])

ans = 0

for word in wordList:
    if score(word) in triangles:
        ans += 1

print(f"There are {ans} triangular words in that list.")