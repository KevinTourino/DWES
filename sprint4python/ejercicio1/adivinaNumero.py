import random

def jugar():
    print("El programa pensará un número entre 1 y un máximo que tú elijas. Intenta adivinarlo con la menor cantidad de intentos posible.")

    while True:
        nivel = input("Elige un nivel de dificultad (fácil, medio, difícil): ").lower()
        if nivel in ["fácil", "facil"]:
            max_num = 50
            break
        elif nivel == "medio":
            max_num = 100
            break
        elif nivel in ["dificil", "difícil"]:
            max_num = 500
            break
        else:
            print("Entrada no válida. Por favor, elige entre 'fácil', 'medio' o 'difícil'.")

    numeroAleatorio = random.randint(1, max_num)

    intentos = 0

    while True:
        try:
            eleccion = int(input(f"\nAdivina el número entre 1 y {max_num}: "))
            intentos += 1

            if (eleccion > 0) and (eleccion < max_num):
                if eleccion < numeroAleatorio:
                    print("Demasiado bajo.")
                elif eleccion > numeroAleatorio:
                    print("Demasiado alto.")
                else:
                    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                    break

            else:
                print(f"Escoge un número comprendido entre el 0 y {max_num}")

        except ValueError:
            print("Por favor, introduce un número entero válido.")

    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez == 's':
        jugar()
    else:
        print("¡Gracias por jugar! ¡Hasta la próxima!")


def main():
    jugar()

if __name__ == "__main__":
    main()