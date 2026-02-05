
import funciones
"""Proyecto llamado task manager pro, que permite gestionar 
tareas y tener persistencia de datos atraves de un archivo JSON"""

def menu():
    tareas = funciones.cargar_tareas()

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
            funciones.mostrar_tareas(tareas)
        elif opcion == "2":
            funciones.agregar_tarea(tareas)
        elif opcion == "3":
            print("Falta implementar")
            #Ecompletar_tarea(tareas)
        elif opcion == "4":
            funciones.eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()


