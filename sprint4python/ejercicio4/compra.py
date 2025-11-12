def menu():
    print("Menú del Gestor de Lista de la Compra")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")

def añadir(lista):
    producto = input("Introduce el nombre del producto a añadir: ").strip().lower()
    if producto in lista:
        print(f"El producto '{producto}' ya está en la lista.")
    else:
        lista.append(producto)
        print(f"Producto '{producto}' añadido a la lista.")

def eliminar(lista):
    producto = input("Introduce el nombre del producto a eliminar: ").strip().lower()
    if producto in lista:
        lista.remove(producto)
        print(f"Producto '{producto}' eliminado de la lista.")
    else:
        print(f"El producto '{producto}' no está en la lista.")

def lista(lista):
    if lista:
        print("Lista de la compra:")
        for producto in sorted(lista):
            print(producto)
    else:
        print("La lista está vacía.")

def eliminarLista(lista):
    confirmacion = input("¿Estás seguro de que quieres vaciar la lista? (s/n): ").lower()
    if confirmacion == 's':
        lista.clear()
        print("La lista ha sido vaciada.")
    else:
        print("Operación cancelada. La lista no ha sido modificada.")

def compra():
    listaCompra = []

    while True:
        menu()

        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                añadir(listaCompra)
            elif opcion == 2:
                eliminar(listaCompra)
            elif opcion == 3:
                lista(listaCompra)
            elif opcion == 4:
                eliminarLista(listaCompra)
            elif opcion == 5:
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
        except ValueError:
            print("Por favor, elige una opción válida.")

if __name__ == "__main__":
    compra()
