from random import choice

def mostrar_tab(tablero):
    for fila in tablero:
        print(fila)
    print()


def meter_jugada(tablero):
    while True:
        try:
            jugada = int(input("Ingresa tu jugada (1-9): "))
        except ValueError:
            print("Escribe un número entero.")
            continue

        if jugada < 1 or jugada > 9:
            print("La jugada debe estar entre 1 y 9.")
            continue

        indice = jugada - 1
        fila = indice // 3
        columna = indice % 3

        if tablero[fila][columna] in ("X", "O"):
            print("Casilla ya ocupada.")
            continue

        tablero[fila][columna] = "O"
        return


def hay_ganador(tablero, ficha):
    for i in range(3):
        # Comprueba la fila i.
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == ficha:
            return True

        # Comprueba la columna i.
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == ficha:
            return True

    # Comprueba las dos diagonales.
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha:
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha:
        return True

    return False


def casillas_libres(tablero):
    libres = []

    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ("X", "O"):
                libres.append((fila, columna))

    return libres


def main():
    tablero = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print("Vamos a jugar al TicTacToe - Tres en raya.")
    print("Jugador: O | Máquina: X")

    tablero[1][1] = "X"
    mostrar_tab(tablero)

    while True:
        # Turno del jugador.
        meter_jugada(tablero)
        mostrar_tab(tablero)

        if hay_ganador(tablero, "O"):
            print("¡Ganó el jugador!")
            break

        libres = casillas_libres(tablero)
        if not libres:
            print("Empate.")
            break

        # Turno de la máquina.
        fila, columna = choice(libres)
        tablero[fila][columna] = "X"
        numero_casilla = fila * 3 + columna + 1
        print(f"La máquina jugó en la casilla {numero_casilla}.")
        mostrar_tab(tablero)

        if hay_ganador(tablero, "X"):
            print("¡Ganó la máquina!")
            break

        if not casillas_libres(tablero):
            print("Empate.")
            break


if __name__ == "__main__":
    main()