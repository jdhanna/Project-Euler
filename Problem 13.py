# Problem: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# Solution: Much of the work here will be scraping the large array of numbers from the website.

from urllib.request import urlopen

def scrapeList():
    url = "https://projecteuler.net/problem=13"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    startCode = '<div class="monospace center">' # If there's an update to the CSS, change this to the class of formatting for the problem text
    endCode = '</div>'

    start_index = html.find(startCode) + len(startCode) +1
    end_index = html[start_index: start_index + 12000].find(endCode)


    #Now scrape out the </ br>
    relevantSection = html[start_index:start_index + end_index]
    a = 0
    b = 1
    array = list()
    while b > 0:
        b = relevantSection[a:].find('<br />')
        array.append(relevantSection[a:a+b])
        a = a + b + 7

    return array[0:100]

array = scrapeList()
# Now python can handle the heavy-duty arithmetic here.
total = 0
for item in array:
    total += int(item)
answer = str(total)[0:10]

print(f'The sum of the array is {total} and the first 10 digits are {answer}')

