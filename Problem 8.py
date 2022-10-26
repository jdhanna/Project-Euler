from urllib.request import urlopen


#Problem statement:

# The four adjacent digits in the large number below that have the greatest product are 9 x 9 x 8 x 9 = 5832

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# Solution:

# We will lose precision storing this as an integer, therefore we store this as a string.
# I'll also scrape the number from the Project Euler Home page rather than copy and paste and formatting.

def scrapeInt(mockObject = False):
    # If Project Euler goes down, I want to be able to run tests on the script anyway
    if mockObject == True:
        return 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843

    url = "https://projecteuler.net/problem=8"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    startCode = '<p class="monospace center">' # If there's an update to the CSS, change this to the class of formatting for the problem text
    endCode = '</p>'

    start_index = html.find(startCode) + len(startCode) +1
    end_index = html[start_index: start_index + 1200].find(endCode)

    #Now scrape out the </ br>
    relevantSection = html[start_index:start_index + end_index]
    a = 0
    b = 1

    largeNumber = str()
    while b > 0:
        b = relevantSection[a:].find('<br />')
        largeNumber = largeNumber + relevantSection[a:a+b]
        a = a + b + 7

    return largeNumber

def stringProduct(s):
    #Given a string s, find it's product.
    answer = 1
    for item in s:
        answer *= int(item)
    return answer



def largestProductOfSize(n, largeNumber):
    a = 0
    best = 0
    for a in range(len(largeNumber) - n + 1):
        test = stringProduct(largeNumber[a:a+n])
        if test > best:
            best = test
    return best

def main():
    largeNumber = scrapeInt()
    print(largestProductOfSize(4, largeNumber)) # Verify that this equals 5832 as they suggest.
    print(largestProductOfSize(13, largeNumber))
    return

main()


