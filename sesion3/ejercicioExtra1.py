# SISTEMAS DE GESTION DE TAREAS

# Definir la lista de tareas
tareas = []

while True:
  print("\nSistema de Gestión de Tareas")
  print("1. Añadir tarea")
  print("2. Listar tareas")
  print("3. Salir")
  opcion = input("Selecciona una opción: ")

  if opcion == "1":
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    tarea = {
      "titulo": titulo,
      "descripcion": descripcion,
      "completada": False
    }
    tareas.append(tarea)
    print("Tarea: ", titulo,  "añadida.")

  elif opcion == "2":
    if not tareas:
      print("No hay tareas.")
    else:
      for tarea in tareas:
        estado = "completada" if tarea["completada"] else "pendiente"
        print("Título: ", tarea['titulo'], "Descripción: ", tarea['descripcion'], "Estado: ", estado)

  elif opcion == "3":
    print("Saliendo del sistema de gestión de tareas.")
    break

  else:
    print("Opción no válida. Intenta de nuevo.")


