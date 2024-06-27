
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

n1 = input()
n2 = input()

print(lockMoves(n1, n2, ["0000"]))