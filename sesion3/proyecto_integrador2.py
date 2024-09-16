# AGREGAR CLIENTE CON VALIDACIONES + SISTEMA DE OPCIONES

################################# AGREGADO 3⬇️ #################################
clientes = []

while True:
  print("Opciones:")
  print("1. Agregar un cliente nuevo")
  print("2. Mostrar todos los clientes agregados")
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
      cliente = { 
        "nombre": nombre,
        "email": email,
        "celular": int(celular)
      }
      clientes.append(cliente)
      ################################# AGREGADO 3⬆️ #################################

      print("Cliente agregado exitosamente")
    else:
      # Datos inválidos
      print("Los datos son inválidos. Vuelve a ingresar los datos.")

  ################################# AGREGADO 3⬇️  #################################
  elif opcion == "2":
    print('Se escogió mostrar todos los clientes agregados')
    # Mostrar todos los clientes guardados
    print("Clientes guardados:")
    for cadaElemento in clientes:
      print(cadaElemento)

  elif opcion == "3":
    # Salir
    print("Se escogió salir del programa")
    break

  else:
    print("Opción no es válida. Por favor, seleccione una opción válida.")
  ################################# AGREGADO 3⬆️ #################################