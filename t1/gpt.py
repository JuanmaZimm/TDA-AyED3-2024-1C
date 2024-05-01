class Jugador:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa

def main():
    # Función recursiva para seleccionar la mejor formación de jugadores
    def select_best_formation(jugadores):
        # Función auxiliar recursiva para realizar el backtracking
        def backtrack(index, formacion_actual, mejores_atacantes, mejores_defensores):
            nonlocal best_attackers, best_defenders, best_formation

            # Caso base: si hemos seleccionado a todos los jugadores
            if index == len(jugadores):
                # Verificar si esta formación es mejor que la actual
                if len(mejores_atacantes) == 5 and len(mejores_defensores) == 5:
                    ataque_total = sum(j.ataque for j in mejores_atacantes)
                    defensa_total = sum(j.defensa for j in mejores_defensores)
                    if ataque_total > best_attackers or \
                            (ataque_total == best_attackers and defensa_total > best_defenders):
                        best_attackers = ataque_total
                        best_defenders = defensa_total
                        best_formation = formacion_actual[:]
                return

            # Caso recursivo: probar seleccionar o no seleccionar al jugador en la posición index
            jugador = jugadores[index]

            # Intentar seleccionar al jugador como atacante
            if len(mejores_atacantes) < 5:
                formacion_actual.append(jugador)
                mejores_atacantes.append(jugador)
                backtrack(index + 1, formacion_actual, mejores_atacantes, mejores_defensores)
                formacion_actual.pop()
                mejores_atacantes.pop()

            # Intentar seleccionar al jugador como defensor
            if len(mejores_defensores) < 5:
                formacion_actual.append(jugador)
                mejores_defensores.append(jugador)
                backtrack(index + 1, formacion_actual, mejores_atacantes, mejores_defensores)
                formacion_actual.pop()
                mejores_defensores.pop()

            # No seleccionar al jugador en esta posición
            backtrack(index + 1, formacion_actual, mejores_atacantes, mejores_defensores)

        # Variables para almacenar la mejor formación
        best_attackers = 0
        best_defenders = 0
        best_formation = []

        # Iniciar el proceso de backtracking
        backtrack(0, [], [], [])

        return best_formation

    # Guardado del input
    casos = int(input())
    for caso in range(1, casos + 1):
        jugadores = []
        for _ in range(10):
            nombre, ataque, defensa = input().split(" ")
            jugador = Jugador(nombre, int(ataque), int(defensa))
            jugadores.append(jugador)

        # Obtener la mejor formación
        best_formation = select_best_formation(jugadores)

        # Imprimir la mejor formación
        print(f"Case {caso}:")
        print("(" + ",".join([j.nombre for j in best_formation[:5]]) + ")")
        print("(" + ",".join([j.nombre for j in best_formation[5:]]) + ")")

if __name__ == "__main__":
    main()
