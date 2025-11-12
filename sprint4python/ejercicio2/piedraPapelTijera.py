import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

reglas = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["piedra", "tijera"]
}

def determinarGanador(usuario, maquina):
    if usuario == maquina:
        return 0
    elif maquina in reglas[usuario]:
        return 1
    else:
        return -1

def jugar_ronda():
    while True:
        eleccionUsuario = input("Elige tu jugada (piedra, papel, tijera, lagarto, spock): ").lower()
        if eleccionUsuario in opciones:
            break
        else:
            print("Opción no válida. Por favor, elige entre 'piedra', 'papel', 'tijera', 'lagarto' o 'spock'.")

    eleccionMaquina = random.choice(opciones)

    print(f"Tu jugada: {eleccionUsuario}")
    print(f"La jugada de la CPU: {eleccionMaquina}")

    resultado = determinarGanador(eleccionUsuario, eleccionMaquina)

    if resultado == 0:
        print("¡Es un empate!")
    elif resultado == 1:
        print("¡Ganaste esta ronda!")
    else:
        print("¡La CPU gana esta ronda!")

    return resultado


def jugar_partida():
    while True:
        try:
            n = int(input("¿Cuántas rondas deseas jugar? (Debe ser un número impar mayor o igual a 1): "))
            if n >= 1 and n % 2 == 1:
                break
            else:
                print("El número de rondas debe ser un número impar mayor o igual a 1.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    victoriaJugador = 0
    victoriaMaquina = 0
    rondasTotales = n // 2 + 1

    while victoriaJugador < rondasTotales and victoriaMaquina < rondasTotales:
        resultado = jugar_ronda()

        if resultado == 1:
            victoriaJugador += 1
        elif resultado == -1:
            victoriaMaquina += 1

        print(f"Marcador: Usuario {victoriaJugador} - CPU {victoriaMaquina}")

    if victoriaJugador > victoriaMaquina:
        print("¡Felicidades! ¡Ganaste la partida!")
    else:
        print("¡La CPU gana la partida!")


def jugar():
    while True:
        jugar_partida()

        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez != 's':
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break


if __name__ == "__main__":
    jugar()
