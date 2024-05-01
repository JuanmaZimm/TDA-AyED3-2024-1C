def max_acorns_collected(grid, t, h, f):
    dp = [[0] * h for _ in range(t)]
    for i in range(h):
        dp[t - 1][i] = grid[t - 1][i]
    for i in range(t - 2, -1 , -1):
        for j in range(h):
            dp[i][j] = grid[i][j] + dp[i + 1][j]
            for k in range(h):
                if j != k:
                    dp[i][j] = max(dp[i][j], grid[i][j] + dp[i + 1][k] - f)
    for row in dp:
        print(row)
    return max(dp[0])

grid = [
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 2, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0]
]

t = len(grid)
h = len(grid[0])
f = 2

result = max_acorns_collected(grid, t, h, f)
print(result)


# def main():
#     datasets = int(input())
#     rtas = []
#     for _ in range(datasets):
#         t, h, f = list(map(int, input().split(" ")))
#         grid = []  # matriz de h x t
#         for _ in range(t):
#             acorns = list(map(int, input().split(" ")))
#             row = [0] * h
#             for a in acorns[1:]:
#                 row[a - 1] += 1
#             grid.append(row)
#         for row in grid:
#             print(row)
#         rtas.append(max_acorns_collected(grid, t, h, f))
#     print(rtas)


# main()

"""
1
3 10 2
3 1 4 10
6 3 5 7 8 9 9
5 3 4 5 6 9
"""
