# AGREGAR CLIENTE CON VALIDACIONES + SISTEMA DE OPCIONES

################################# AGREGADO 3⬇️ #################################
usuarios = []

while True:
  print("Opciones:")
  print("1. Agregar un usuario nuevo")
  print("2. Mostrar todos los usuarios")
  print("3. Salir")

  opcion = input("Seleccione una opción (1/2/3): ")

  if opcion == "1":
  ################################# AGREGADO 3⬆️ #################################
    # Ingresar nombre, e-mail, teléfono
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el e-mail: ")
    celular = input("Ingrese el celular: ")

    # Validamos los datos (formato e-mail, campos obligatorios)
    datos_validos = True

    # Verificar que el nombre no esté vacío
    if len(nombre) == 0:
      datos_validos = False

    # Verificar que el e-mail contenga '@' y '.'
    if '@' not in email or '.' not in email:
      datos_validos = False

    # Verificar que el teléfono tenga 9 dígitos
    if len(celular) != 9:
      datos_validos = False

    # Decisión basada en la validez de los datos
    if datos_validos:
      # Registramos cliente
      ################################# AGREGADO 3⬇️ #################################
      usuario = { 
        "nombre": nombre,
        "email": email,
        "celular": int(celular)
      }
      usuarios.append(usuario)
      ################################# AGREGADO 3⬆️ #################################

      print("Cliente agregado exitosamente")
    else:
      # Datos inválidos
      print("Datos inválidos. Vuelve a ingresar los datos.")

  ################################# AGREGADO 3⬇️  #################################
  elif opcion == "2":
    # Mostrar todos los usuarios guardados
    print("Usuarios guardados:")
    for usuario in usuarios:
      print(usuario)

  elif opcion == "3":
    # Salir
    print("Saliendo del programa.")
    break

  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
  ################################# AGREGADO 3⬆️ #################################