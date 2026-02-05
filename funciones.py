import os
import json

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

def agregar_tarea(tareas):
    titulo = input("\nEscribe el título de la tarea: ")
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("Tarea agregada correctamente.")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        tarea_id = int(input("\nIngresa el ID de la tarea completada: "))
        for tarea in tareas:
            if tarea["id"] == tarea_id:
                tarea["completada"] = True
                guardar_tareas(tareas)
                print("Tarea marcada como completada.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("Ingresa un número válido.")
