def mgn(c: int, j: int, P: list, M: list) -> int:
    if M[c][j] != float('-inf'):
        return M[c][j]
    elif (c < 0 or c > j):
        return float('-inf')
    elif c == j == 0:
        return 0
    else:
        return max(mgn(c - 1, j - 1, P, M) - P[j], mgn(c + 1, j - 1, P, M) + P[j], mgn(c, j - 1, P, M))


def crearMatriz(P: list, M: list) -> list:
    n = len(P)

    for j in range(n):
        M[0][j] = mgn(0, j, P, M)

    for c in range(1, n):
        for j in range(c, n):
            M[c][j] = mgn(c, j, P, M)
    return M


P = [0, 3, 2, 5, 6]
n = len(P)
M = [[float('-inf') for _ in range(n)] for _ in range(n)]
M.append([float('-inf') for _ in range(n)])
matrix = crearMatriz(P, M)
matrixNueva = crearMatriz(P, matrix)
for row in matrix:
    print(row)

print