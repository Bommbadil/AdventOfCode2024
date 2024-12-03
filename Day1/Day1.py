#### Part 1
list1 = []
list2 = []
list3 = []

with open(r'E:\\AdventOfCode2024\\Day1\\input_day1.txt', 'r') as lines:
    text = lines.readlines()
    for line in text:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

for i in range(len(list1)):
    list3.append(abs(list1[i] - list2[i]))

print(sum(list3))


#### Part 2
list4 = []
for num in list1:
    list4.append(list2.count(num)*num)

print(sum(list4))