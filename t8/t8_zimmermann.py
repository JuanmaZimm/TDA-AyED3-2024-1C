cases:int = input()
answers: int = []

for case in cases:
    line: str = input().split(' ')
    n: int = int(line[0])
    codes: list = [int(x) for x in line[1:]]

for i in cases:
    print(cases[i])