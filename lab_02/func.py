def get_Kolmogorov_coeffs(matrix):
    n = len(matrix)

    new_matrix = []

    for i in range(n):
        for j in range(n):
            if i == j:
                new_matrix[i][j] = -sum([row[i] for row in matrix])
            else:
                new_matrix[i][j] = matrix[i][j]

    return [matrix[j][i] if j != i else -sum(matrix[i]) for j in range(n)]
        if i != (n - 1) else [1 for i in range(n)]
