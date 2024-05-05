def comparar(a: str, b: str) -> str:
    if (a == b):
        return True

    if (len(a) % 2 != 0 or len(b) % 2 != 0):
        return False

    mitad: int = len(a) // 2

    return (comparar(a[:mitad], b[mitad:]) and comparar(a[mitad:], b[:mitad])) or (comparar(a[:mitad], b[:mitad]) and comparar(a[mitad:], b[mitad:]))


a: str = input()
b: str = input()
if (comparar(a, b)):
    print("YES")
else:
    print("NO")
