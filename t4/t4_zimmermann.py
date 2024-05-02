def compararAux(a: str, b: str) -> str:
    if (a == b):
        return True
    else:
        return sorted(a) == sorted(b)


def comparar(a: str, b: str) -> str:
    if (a == a):
        return "YES"
    else:
        a1: str = a[:len(a)//2]
        a2: str = a[len(a)//2:]
        b1: str = b[:len(b)//2]
        b2: str = b[len(b)//2:]
        if ((a1 == b1 and a2 == b2) or (a1 == b2 and a2 == b1)):
            return "YES"
        else:
            return "NO"


a: str = input()
b: str = input()
if (a == b):
    print("YES")
else:
    print(comparar(a, b))
