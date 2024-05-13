def backtrack(M, I, k, suma):
    if len(I) == k:
        return I

    max_I = []
    max_sum = suma
    for i in range(len(M)):
        if i not in I and len(I) < k:
            new_I = I + [i]
            new_sum = max_sum + sum(M[i][j] for j in I) + sum(M[j][i] for j in I)
            if new_sum > max_sum:
                max_sum = new_sum
                result = backtrack(M, new_I, k, new_sum)
                max_I = result

    return max_I


def maximize_sum(M, k):
    return backtrack(M, [], k, 0)


# Ejemplo de uso:
matrix = [
    [0, 1, 10, 10],
    [1, 0, 2, 5],
    [10, 2, 0, 1],
    [10, 5, 1, 0]
]
k = 3
print("Suma máxima:", maximize_sum(matrix, k))
