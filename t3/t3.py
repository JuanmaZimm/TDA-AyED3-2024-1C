# def max_acorns_collected(grid, t, h, f):
#     aux = [[0] * h for _ in range(t)]

#     for row in range(t):
#         aux[row][h - 1] = grid[row][h - 1]

#     for col in range(h - 2, -1, -1):
#         for row in range(t):
#             max_acorns = aux[row][col + 1]

#             for arbol in range(t):
#                 if arbol != row and col + f < h:
#                     max_acorns = max(max_acorns, aux[arbol][col + f])

#             aux[row][col] = max_acorns + grid[row][col]

#     # max_total_acorns = max(aux[row][0] for row in range(t))
#     return max(aux[row][0] for row in range(t))


def max_acorns_collected(grid, t, h, f):
    aux = [[0] * h for _ in range(t)]
    max_per_h = [0] * h

    for row in range(t):
        aux[row][h - 1] = grid[row][h - 1]

    for col in range(h - 2, -1, -1):
        for arbol in range(t):
            if col + f < h:
                aux[arbol][col] = grid[arbol][col] + max(aux[arbol][col + 1], max_per_h[col + f])
            else:
                aux[arbol][col] = grid[arbol][col] + max(aux[arbol][col + 1], 0)
            max_per_h[col] = max(max_per_h[col], aux[arbol][col])

    res = 0
    for arbol in range(t):
        res = max(res, aux[arbol][0])
    return res


def main():
    datasets = int(input())
    rtas = []
    for _ in range(datasets):
        t, h, f = list(map(int, input().split(" ")))
        grid = []
        for _ in range(t):
            acorns = list(map(int, input().split(" ")))
            row = [0] * h
            for a in acorns[1:]:
                row[a - 1] += 1
            grid.append(row)
        rtas.append(max_acorns_collected(grid, t, h, f))
    final_input = int(input())
    if final_input == 0:
        for rta in rtas:
            print(rta)


main()

"""
1
3 10 2
3 1 4 10
6 3 5 7 8 9 9
5 3 4 5 6 9
"""
