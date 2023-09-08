# Задание 1.
# Напишите функцию для транспонирования матрицы.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transposition_matrix(matrix):
    trans_matrix = [[0 for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


print(*transposition_matrix(matrix), sep='\n')
