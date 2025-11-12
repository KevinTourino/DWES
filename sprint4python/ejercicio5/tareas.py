class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrarInformacion(self):
        if self.completada:
            estado = "completada"
        else:
            estado = "pendiente"
        return f"Título: {self.titulo} - Estado: {estado}"

    def marcar(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion

def menu():
    print("Menú del Gestor de Tareas")
    print("1. Crear tarea")
    print("2. Mostrar todas")
    print("3. Marcar como completada")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

def crear(tareas):
    titulo = input("Introduce el título de la tarea: ").strip()
    descripcion = input("Introduce la descripción de la tarea: ").strip()
    nueva_tarea = Tarea(titulo, descripcion)
    tareas.append(nueva_tarea)
    print("Tarea creada con éxito.")

def mostrar(tareas):
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        for tarea in tareas:
            print(tarea.mostrarInformacion())

def marcar(tareas):
    titulo = input("Introduce el título de la tarea que quieres marcar como completada: ").strip().lower()
    tareaEncontrada = False
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tarea.marcar()
            print("La tarea ha sido marcada como completada.")
            tareaEncontrada = True
            break
    if not tareaEncontrada:
        print("Tarea no encontrada.")

def editar(tareas):
    titulo = input("Introduce el título de la tarea que quieres editar: ").strip().lower()
    tareaEncontrada = False
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            nuevoTitulo = input("Introduce el nuevo título: ").strip()
            nuevaDescripcion = input("Introduce la nueva descripción: ").strip()
            tarea.editar(nuevoTitulo, nuevaDescripcion)
            print("Tarea actualizada con éxito.")
            tareaEncontrada = True
            break
    if not tareaEncontrada:
        print("Tarea no encontrada.")

def eliminar(tareas):
    titulo = input("Introduce el título de la tarea que quieres eliminar: ").strip().lower()
    tareaEncontrada = False
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tareas.remove(tarea)
            print("Tarea eliminada con éxito.")
            tareaEncontrada = True
            break
    if not tareaEncontrada:
        print("Tarea no encontrada.")

def tareas():
    tareas = []
    while True:
        menu()
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                crear(tareas)
            elif opcion == 2:
                mostrar(tareas)
            elif opcion == 3:
                marcar(tareas)
            elif opcion == 4:
                editar(tareas)
            elif opcion == 5:
                eliminar(tareas)
            elif opcion == 6:
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción no válida, por favor elige entre 1 y 6.")
        except ValueError:
            print("Por favor, ingresa un número válido para elegir la opción.")

if __name__ == "__main__":
    tareas()
