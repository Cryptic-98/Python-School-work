matrix1 = [
    [1, 3, 5],
    [3, 1, 5],
    [5, 3, 1]
]
matrix2 = [
    [2, 4, 6],
    [4, 2, 6],
    [6, 4, 2]
]


def add_matrix(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        new_row = []
        for j in range(len(matrix1[i])):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)

    return result


result_matrix = add_matrix(matrix1, matrix2)
print(result_matrix)
