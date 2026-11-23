# python-tic-tac-toe
Juego del tres en raya por consola, ejercicio práctico basado en el proyecto final del curso de Python Essentials 1 de Cisco.

## Funcionamiento

- El jugador utiliza O y la máquina utiliza X.
- La máquina comienza colocando su ficha en el centro.
- El jugador elige una casilla disponible del 1 al 9.
- La máquina selecciona sus siguientes movimientos aleatoriamente.
- La partida termina cuando alguien consigue tres fichas en línea o se produce un empate.

El programa comprueba las entradas incorrectas, los números fuera de rango y las casillas ocupadas.

## Cómo ejecutarlo

Necesitas Python 3. El programa utiliza únicamente la biblioteca estándar.

Descarga el repositorio, abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python TicTacToe.py
```

En Linux, puedes utilizar:

```bash
python3 TicTacToe.py
```

## Organización del código

- `mostrar_tab`: muestra el tablero.
- `meter_jugada`: solicita y valida la jugada del usuario.
- `hay_ganador`: comprueba filas, columnas y diagonales.
- `casillas_libres`: devuelve las coordenadas de las casillas disponibles.
- `main`: organiza los turnos y el final de la partida.

## Conceptos practicados

Funciones, listas anidadas, tuplas, bucles, condicionales, manejo de excepciones y selección aleatoria.

## Autor
Álvaro Ahedo Sevilla — Ahed0
