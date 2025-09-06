# gestor_tareas.py

tareas = []

def mostrar_tareas():
    print("\n📋 Lista de tareas:")
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "✔️" if tarea["completada"] else "❌"
            print(f"{i}. {tarea['nombre']} [{estado}]")

def agregar_tarea(nombre):
    tareas.append({"nombre": nombre, "completada": False})
    print(f"Tarea '{nombre}' agregada ✅")

def completar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print(f"Tarea '{tareas[indice]['nombre']}' completada ✔️")
    else:
        print("Índice inválido ❌")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        print(f"Tarea '{tarea['nombre']}' eliminada 🗑️")
    else:
        print("Índice inválido ❌")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            nombre = input("Escribe el nombre de la tarea: ")
            agregar_tarea(nombre)
        elif opcion == "3":
            mostrar_tareas()
            indice = int(input("Número de tarea a completar: ")) - 1
            completar_tarea(indice)
        elif opcion == "4":
            mostrar_tareas()
            indice = int(input("Número de tarea a eliminar: ")) - 1
            eliminar_tarea(indice)
        elif opcion == "5":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida ❌")

if __name__ == "__main__":
    menu()
