''' Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. 
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов 
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению. '''

import copy
matrix = []
line = []
while line != ['end']:
    line = [i for i in input().split()]
    if line != ['end']:
        matrix.append(line)
# организовать второй список для вывода
matrix1 = copy.deepcopy(matrix)
# -----
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix1[i][j] = int(matrix[i][(j+1) % len(matrix[i])]) + int(matrix[(i+1) % len(matrix)][j]) + int(matrix[i][(j-1) % len(matrix[i])]) + int(matrix[(i-1) % len(matrix)][j])
# -----
for k in range(len(matrix1)):
    for s in range(len(matrix1[k])):
        print(matrix1[k][s], end=" ")
    print()
    
