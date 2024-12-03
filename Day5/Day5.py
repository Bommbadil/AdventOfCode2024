

def sumup(sortedpages):
    total_sum = 0
    for page in sortedpages:
        if(len(page)%2 == 0):
            continue
        index = int((len(page) - 1) / 2)
        total_sum += page[index]
    return total_sum

# Im Dictionary nachschauen
def pagechecker(rules, pages):
    indices = []
    sorted = []
    for page in pages:
        for i in range(len(page) - 1):
            value = str(page[i + 1])
            key = str(page[i])
            if value not in rules.get(key, []):
                break
            if i == (len(page) - 2):
                indices.append(pages.index(page))
    for index in indices:
        sorted.append(pages[index])

    return sorted

with open(r'E:\\AdventOfCode2024\\Day5\\input.txt', 'r') as lines:
    text = lines.readlines()

rules = dict()
tuples = []
pagesRaw = []

# Dictionary befüllen
for line in text:
    if '|' in line:
        line = line.strip()
        key, value = line.split('|')
        if key in rules:
            rules[key].append(value)
        else:
            rules[key] = [value]

# Pages befüllen
for line in text:
    if not '|' in line:
        pagesRaw.append(line.strip())
pagesRaw.pop(0)
pages = [list(map(int, item.split(','))) for item in pagesRaw]

#print(pagechecker(rules, pages))
#print(sumup(pagechecker(rules, pages)))


def getunsorted(rules, pages):
    indices = []
    unsorted = []
    for page in pages:
        for i in range(len(page) - 1):
            value = str(page[i + 1])
            key = str(page[i])
            if value not in rules.get(key, []):
                indices.append(pages.index(page))
                break
    for index in indices:
        unsorted.append(pages[index])

    return unsorted

def singlepagechecker(rules, page):
    for i in range(len(page) - 1):
        value = str(page[i + 1])
        key = str(page[i])
        if value not in rules.get(key, []):
            return False
    return True

def sortpages(rules, pages):
    for page in pages:
        while not singlepagechecker(rules, page):
            for i in range(len(page) - 1):
                value = str(page[i + 1])
                key = str(page[i])
                if value not in rules.get(key, []):
                    page[i], page[i + 1] = page[i + 1], page[i]
    return pages


unsorted = getunsorted(rules, pages)
print('UNSORTED' + str(unsorted))
print('SORTED' + str(sortpages(rules, unsorted)))
print(str(sumup(sortpages(rules, unsorted))))