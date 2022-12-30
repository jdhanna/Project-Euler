# Problem 12: p022_names.txt is a text file containing over 5 thousand first names. Begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list ot obtain a "name score"

# For example, when sorted into alphabetical order, "COLIN" is worth 3 + 15 + 12 + 9 + 14 = 53 is the 938th name on the list
# so COLIN would score 938x53 = 49714.

# What is the total of all the name scores in the file?

# Solution: There's no trick here, just some arcane requirements.

def readFile(path):
    with open(path) as f:
        rawText = f.readlines()
        rawText = rawText[0]
    return rawText


def stringToList(rawText):
    names = list()
    a = 0
    b = 1
    while b != -1:  # Some care is needed here to strip out the quotes and commas, and not incorrectly cut off the last name.
        c = rawText[a + 1:].find('"')
        nextName = rawText[a + 1:a + c + 1]
        names.append(nextName)
        b = rawText[a:].find(',')
        a = a + b + 1
    return names


def alphabetize(names):
    return sorted(names)


def scoreName(str):
    ans = 0
    for letter in str:
        ans += ord(letter) - 64
    return ans


def weightAllNames(lst):
    ans = 0
    for i in range(0, len(lst)):
        # print(f"{i+1}th Name: {lst[i]}")
        ans = ans + (i + 1) * (scoreName(lst[i]))
    return ans


def main():
    raw_test = readFile("Data/p022_names.txt")
    names = stringToList(raw_test)
    names = alphabetize(names)
    print(weightAllNames(names))
    return


main()
