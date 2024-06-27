def lockMoves(n1: str, n2: str, unlocked: list) -> int:
    if n2 in unlocked:
        return 0
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

for i in range(cases):
    line: str = input().split(' ')
    n: int = int(line[0])
    codes: list = line[1:]
    answers.append(minMoves(n, codes))

for i in range(len(answers)):
    print(answers[i])

"""
4
2 1155 2211
3 1111 1155 5511
3 1234 5678 9090
4 2145 0213 9113 8113
"""
