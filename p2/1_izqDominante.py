def izqDominante(list: list) -> bool:
    if (len(list) == 2):  # O(1)
        return list[0] > list[1]  # O(1)
    n = len(list)  # O(1)
    half1 = list[:n//2]  # O(n)
    half2 = list[n//2:]  # O(n)
    if sum(half1) <= sum(half2):  # O(n)
        return False
    else:
        return izqDominante(half1) and izqDominante(half2)  # O(1)

# T(n) = 2T(n/2) + O(n) = O(nlogn)


ejemplo1: list = [8, 6, 7, 4, 5, 1, 3, 2]
ejemplo2: list = [8, 4, 7, 6, 5, 1, 3, 2]

print(izqDominante(ejemplo1))  # True
print(izqDominante(ejemplo2))  # False
