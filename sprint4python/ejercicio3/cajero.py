def menu():
    print("Menú del Cajero Automático")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def saldo(cuenta):
    print(f"Saldo actual: ${cuenta['saldo']}")

def ingresar(cuenta):
    while True:
        try:
            cantidad = float(input("¿Cantidad a ingresar?: "))
            if cantidad > 0:
                cuenta['saldo'] += cantidad
                print(f"Has ingresado ${cantidad}. Saldo actualizado: ${cuenta['saldo']}")
                break
            else:
                print("El dinero a ingresar debe ser positivo.")
        except ValueError:
            print("Por favor, ingresa una cantidad válida.")

def retirar(cuenta):
    while True:
        try:
            cantidad = float(input("¿Cantidad a retirar?: "))
            if cantidad > cuenta['saldo']:
                print("Saldo insuficiente.")
            elif cantidad > 0:
                cuenta['saldo'] -= cantidad
                print(f"Has retirado ${cantidad}. Saldo restante: ${cuenta['saldo']}")
                break
            else:
                print("El dinero a retirar debe ser positivo.")
        except ValueError:
            print("Por favor, ingresa una cantidad válida.")

def cajero():
    cuenta = {"nombre": "Ana", "saldo": 1200.0}

    while True:
        menu()

        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                saldo(cuenta)
            elif opcion == 2:
                ingresar(cuenta)
            elif opcion == 3:
                retirar(cuenta)
            elif opcion == 4:
                print("¡Gracias por usar el Cajero Automático! ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
        except ValueError:
            print("Por favor, elige una opción válida.")


if __name__ == "__main__":
    cajero()
