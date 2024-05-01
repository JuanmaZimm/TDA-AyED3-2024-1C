def g(L, C):
    tanque = C
    n_estaciones = 0
    estaciones = []
    i = 0
    N = len(L)
    while i < N:
        if tanque > L[i]:
            estaciones.append(i)
            n_estaciones += 1
        tanque -= L[i]
        i += 1
    return estaciones


print(g([10, 20, 30, 40, 50], 25))
