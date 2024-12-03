import re
from functools import reduce

#### Part 1
with open(r'E:\\AdventOfCode2024\\Day3\\input.txt', 'r') as lines:
    text = lines.read()

#mul = re.findall(r"mul\((\d{1,4}),(\d{1,4})\)", text)
multiply = lambda x, y: x * y
#output = [reduce(multiply, map(int, tpl)) for tpl in mul]
#print(sum(output))


#### Part 2
text.replace('\\n', ' ').replace('\\r', '').replace('\r\n', '')
sub = re.sub(r"don't.*?do[^n]", "NOPENOPENOPENOPE", text)
mul2 = re.findall(r"mul\((\d{1,4}),(\d{1,4})\)", sub)
output = [reduce(multiply, map(int, tpl)) for tpl in mul2]
print(sub)
print(sum(output))
