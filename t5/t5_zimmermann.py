def min_work(n: int, casas: list) -> int:
    costo = 0
    suma = [0] * (n + 1)

    for i in range(1, n + 1):
        suma[i] = suma[i - 1] + casas[i - 1]

    for i in range(1, n):
        costo += abs(suma[i])

    return costo


n: int = int(input())
res: list = []
while n > 0:
    casas: list = [int(x) for x in input().split(' ')]
    res.append(min_work(n, casas))

    n = int(input())
for r in res:
    print(r)

# Usuario de vJudge: JuanmaZimm
