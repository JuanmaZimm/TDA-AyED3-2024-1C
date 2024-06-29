def lockMoves(n1: str, n2: str) -> int:
    # Convert numbers to strings for easy digit access
    str_n1, str_n2 = n1.zfill(4), n2.zfill(4)
    total_moves = 0

    # Iterate through each digit to calculate moves
    for digit_n1, digit_n2 in zip(str_n1, str_n2):
        # Calculate absolute difference
        diff = abs(int(digit_n1) - int(digit_n2))
        # Calculate moves (minimum between moving forward or backward)
        moves = min(diff, 10 - diff)
        total_moves += moves
    return total_moves


def costs(n: int, edges: list, nodes: list):
    for v in range(n):
        for w in range(v, n):
            if v != w:
                cost = lockMoves(nodes[v], nodes[w])
                print(f"Cost from {nodes[v]} to {nodes[w]}: {cost}")
                edges[v][w] = cost
                edges[w][v] = cost


def min_edge(nodes: list, edges: list, visited: list):
    min = (0, 0, 1000)
    for v in visited:
        for w in range(len(nodes)):
            if w not in visited:
                if edges[nodes.index(v)][w] < min[2]:
                    min = (nodes.index(v), w, edges[nodes.index(v)][w])
    return min


def prim(n: int, nodes: list, edges: list):
    visited = [nodes[0]]
    edges_visited = []
    tree = []
    while len(visited) < n:
        e = min_edge(visited, edges, visited)
        visited.append(nodes[e[1]])
        edges_visited.append(e)
        tree.append((e[0], e[1]))
    return tree


def minMoves(n: int, codes: list) -> int:
    # Initialize variables
    total_moves = 0
    unlocked = ["0000"]

    # Iterate through each code
    for i in range(n):
        # Calculate moves to unlock
        moves = lockMoves(unlocked[i], codes[i], unlocked)
        options = [lockMoves(u, codes[i], unlocked) for u in unlocked]
        options.append(moves)
        # Update total moves
        total_moves += min(options)
        # Append unlocked code to list
        unlocked.append(codes[i])

    return total_moves


cases: int = int(input())
answers: list = []

for _ in range(cases):
    line: str = input().split(" ")
    n: int = int(line[0])
    nodes: list = line[1:]
    edges: list = [[0] * n for _ in range(n)]  # Matrix

    costs(n, edges, nodes)
    for i in range(n):
        print(edges[i])

    tree: list = prim(n, nodes, edges)
    print(tree)
    nodes.append("0000")

for i in range(len(answers)):
    print(answers[i])

"""
4
2 1155 2211
3 1111 1155 5511
3 1234 5678 9090
4 2145 0213 9113 8113
"""
