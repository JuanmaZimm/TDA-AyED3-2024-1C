def mejorFormacion(jugadores, equipo, index, max_atk, max_def, min_nombre):
    if len(equipo) == 5:
        ataque_actual = sum(jugador[1] for jugador in equipo)
        defensores = [
            jugador for jugador in jugadores if jugador not in equipo]
        defensa_actual = sum(jugador[2] for jugador in defensores)
        nombre_actual = sorted(jugador[0] for jugador in equipo)
        if (ataque_actual > max_atk[0] or
            (ataque_actual == max_atk[0] and defensa_actual > max_def[0]) or
                (ataque_actual == max_atk[0] and defensa_actual == max_def[0] and nombre_actual < min_nombre[0])):
            max_atk[0] = ataque_actual
            max_def[0] = defensa_actual
            min_nombre[0] = nombre_actual
            max_atk[1] = equipo[:]
        return
    if index == len(jugadores):
        return
    equipo.append(jugadores[index])
    mejorFormacion(jugadores, equipo, index + 1,
                   max_atk, max_def, min_nombre)
    equipo.pop()
    mejorFormacion(jugadores, equipo, index + 1,
                   max_atk, max_def, min_nombre)


T = int(input())
res = []
for _ in range(T):
    jugadores = []
    for j in range(10):
        jugador = input().split()
        jugadores.append((jugador[0], int(jugador[1]), int(jugador[2]), j))
    max_atk = [0, []]
    max_def = [0]
    min_nombre = [None]
    mejorFormacion(jugadores, [], 0, max_atk, max_def, min_nombre)
    max_atk_indices = [jugador[3] for jugador in max_atk[1]]
    max_atk[1] = [jugador[0] for jugador in max_atk[1]]
    defensores = []
    for jugador in jugadores:
        if jugador[3] not in max_atk_indices:
            defensores.append(jugador[0])
    res.append("Case " + str(_+1) + ":")
    res.append("(" + ", ".join(sorted(max_atk[1])) + ")")
    res.append("(" + ", ".join(sorted(defensores)) + ")")
print("\n".join(res))
# Usuario de vJudge: JuanmaZimm
