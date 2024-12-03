with open(r'E:\\AdventOfCode2024\\Day6\\input.txt', 'r') as file:
    content = file.read()
    matrix = [list(line.strip()) for line in content.splitlines()]

guard: tuple = (0, 0)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '^':
            guard = (i, j)
            break
    if guard != (0, 0):
        break
guardStart = guard

def guardWalk(guard, newMatrix):
    dir = 1 # 1 = oben, 2 = rechts, 3 = unten, 4 = links
    visited = set()
    while (guard[0] >= 0 and guard[0] < len(newMatrix)) and (guard[1] >= 0 and guard[1] < len(newMatrix[0])):
        if (guard, dir) in visited:
            return True
        visited.add((guard, dir))
        if dir == 1:
            if (not (guard[0] - 1) >= 0 or not (guard[0] - 1) < len(newMatrix)):
                break
            if newMatrix[guard[0] - 1][guard[1]] == '#':
                dir = 2
                continue
            guard = (guard[0] - 1, guard[1])
        elif dir == 2:
            if (not (guard[1] + 1) >= 0 or not (guard[1] + 1) < len(newMatrix[0])):
                break
            if newMatrix[guard[0]][guard[1] + 1] == '#':
                dir = 3
                continue
            guard = (guard[0], guard[1] + 1)
        elif dir == 3:
            if (not (guard[0] + 1) >= 0 or not (guard[0] + 1) < len(newMatrix)):
                break
            if newMatrix[guard[0] + 1][guard[1]] == '#':
                dir = 4
                continue
            guard = (guard[0] + 1, guard[1])
        elif dir == 4:
            if (not (guard[1] - 1) >= 0 or not (guard[1] - 1) < len(newMatrix[0])):
                break
            if newMatrix[guard[0]][guard[1] - 1] == '#':
                dir = 1
                continue
            guard = (guard[0], guard[1] - 1)
    return False

def addObstacles(matrix, start):
    possObs = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '^' and matrix[i][j] != '#':
                new_matrix = [row[:] for row in matrix] 
                new_matrix[i][j] = '#' 

                if guardWalk(start, new_matrix):
                    possObs.add((i,j))
    return possObs

print(len(addObstacles(matrix, guardStart)))






