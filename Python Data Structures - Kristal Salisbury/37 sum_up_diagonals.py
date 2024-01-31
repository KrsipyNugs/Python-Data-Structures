def sum_up_diagonals(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]
    return total


m1 = [
    [1, 2],
    [30, 40],
]
sum_up_diagonals(m1)

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
sum_up_diagonals(m2)