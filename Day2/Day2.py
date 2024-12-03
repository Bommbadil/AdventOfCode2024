#### Part 1
list1 = []
list2 = []
i = 0

def check(list):
    if not all(list[i] < list[i + 1] for i in range(len(list) - 1)) and not all(list[i] > list[i + 1] for i in range(len(list) - 1)):
        return False
    
    if any(not (1 <= abs(list[i] - list[i + 1]) <= 3) for i in range(len(list) - 1)):
        return False
    
    return True

#### Part 2
def fixList(list):
    for i in range(len(list)):
        temp_lst = list[:i] + list[i+1:]  # Splicing = wichtig wenn man Listen dynamisch verändert!!
        if check(temp_lst):  
            list[:] = temp_lst  
            return 1
    
    return 0 

with open(r'E:\\AdventOfCode2024\\Day2\\input.txt', 'r') as lines:
    text = lines.readlines()
    for line in text:
        list1.append(line)

for line in list1:
    list2 = list(map(int, line.strip().split()))
    if check(list2):
        i = i + 1
    else:
        i = i + fixList(list2)
    

print(i)