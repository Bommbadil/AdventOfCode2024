import numpy as np
# ZWISCHENSTAND
def crossmas(matrix):
    crosscount = 0
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[i]) - 3):
            # Überprüfen für "XMAS" (diagonal nach unten rechts) und "SAMX" (diagonal nach unten links)
            if (matrix[i][j] == "X" and matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S") or \
               (matrix[i][j] == "S" and matrix[i+1][j+1] == "A" and matrix[i+2][j+2] == "M" and matrix[i+3][j+3] == "X"):
                crosscount += 1

            # Überprüfen für "XMAS" (diagonal nach oben links) und "SAMX" (diagonal nach oben rechts)
            if (matrix[i][j] == "X" and matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S") or \
               (matrix[i][j] == "S" and matrix[i-1][j-1] == "A" and matrix[i-2][j-2] == "M" and matrix[i-3][j-3] == "X"):
                crosscount += 1

            # Überprüfen für "XMAS" (vertikal nach unten) und "SAMX" (vertikal nach oben)
            if (matrix[i][j] == "X" and matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S") or \
               (matrix[i][j] == "S" and matrix[i+1][j] == "A" and matrix[i+2][j] == "M" and matrix[i+3][j] == "X"):
                crosscount += 1

            # TODO: XMAS nach Zeilenumbruch
    return crosscount

# Lade die Datei
with open(r'E:\\AdventOfCode2024\\Day4\\input.txt', 'r') as file:
    content = file.read()

print(content)

f = np.loadtxt(r'E:\\AdventOfCode2024\\Day4\\input.txt', dtype="str")
matrix = np.array([list(line) for line in f])

# Überprüfe Muster in der Matrix
pattern1 = "XMAS"
pattern2 = "SAMX"
count = content.count(pattern1) + content.count(pattern2) + crossmas(matrix)
print(count)