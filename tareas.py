import json
import os

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print("\nLista de tareas:")
    for tarea in tareas:
        estado = "✅" if tarea["completada"] else "❌"
        print(f'{tarea["id"]}. {tarea["titulo"]} {estado}')


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        tarea_id = int(input("\nIngresa el ID de la tarea a eliminar: "))
        tareas[:] = [t for t in tareas if t["id"] != tarea_id]

        # Reordenar IDs
        for i, tarea in enumerate(tareas):
            tarea["id"] = i + 1

        guardar_tareas(tareas)
        print("Tarea eliminada.")
    except ValueError:
        print("Ingresa un número válido.")


def menu():
    tareas = cargar_tareas()

    while True:
        print("""
TASK MASTER PRO
1. Ver tareas
2. Agregar tarea
3. Completar tarea
4. Eliminar tarea
5. Salir
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            print("Falta implementar")
            #agregar_tarea(tareas)
        elif opcion == "3":
            print("Falta implementar")
            #Ecompletar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()


