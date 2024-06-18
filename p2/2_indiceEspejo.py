def indiceEspejo(list: list, start: int = 0, end: int = None) -> bool:
    if end is None:
        end = len(list) - 1

    if start > end:
        return False

    mid = (start + end) // 2

    if list[mid] == mid:
        return True
    elif list[mid] > mid:
        return indiceEspejo(list, start, mid - 1)
    else:
        return indiceEspejo(list, mid + 1, end)

# T(n) = T(n/2) + O(1) = O(logn) porque la lista está ordenada

ejemplo: list = [-4, -1, 2, 4, 7]
print(indiceEspejo(ejemplo))  # True
