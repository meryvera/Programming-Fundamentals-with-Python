# AGREGAR FUNCIONES

################################# AGREGADO 5 ⬇️ #################################
def ordenar_clientes():
  # Ordena la lista de clientes por número de celular
  clientes.sort(key=lambda x: x["celular"])

def buscar_cliente_por_celular(celular_buscar):
  #Busca un cliente por número de celular usando búsqueda binaria
  izquierda = 0
  derecha = len(clientes) - 1

  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    cliente_medio = clientes[medio]
    print('linea 16 - cliente_medio', cliente_medio)

    if cliente_medio["celular"] == celular_buscar:
      print(cliente_medio)
      return medio # Devuelve el índice del cliente
    elif cliente_medio["celular"] < celular_buscar:
      izquierda = medio + 1
    else:
      derecha = medio - 1

  return None
################################# AGREGADO 5 ⬆️ #################################

# clientes = []
clientes = [
  {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},
  {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567},
  {'nombre': 'adri', 'email': 'adri@hola.com', 'celular': 987654321},
  {'nombre': 'Jose', 'email': 'jose@hola.com', 'celular': 999999999}
]

while True:
  print("Opciones:")
  print("1. Agregar un cliente nuevo")
  print("2. Mostrar todos los clientes")
  print("3. Buscar un cliente por celular")
  print("4. Salir")

  opcion = input("Seleccione una opción (1/2/3/4): ")

  if opcion == "1":
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
      
      cliente = { 
        "nombre": nombre,
        "email": email,
        "celular": int(celular)
      }
      clientes.append(cliente)
      ################################# AGREGADO 5 ⬇️ #################################
      ordenar_clientes() # Ordena la lista después de agregar un nuevo usuario
      ################################# AGREGADO 5 ⬆️ #################################

      print("Cliente agregado exitosamente")
    else:
      # Datos inválidos
      print("Datos inválidos. Vuelve a ingresar los datos.")

  elif opcion == "2":
    # Mostrar todos los clientes guardados
    print("Clientes guardados:")
    for cliente in clientes:
      print(cliente)
  
  ################################# AGREGADO 5 ⬇️  #################################
  elif opcion == "3":
    # Buscar un usuario por número de celular
    celular_buscar = int(input("Ingrese el número de celular del cliente a buscar: "))
    print('celular ingresado x cliente', celular_buscar)
    cliente_encontrado = buscar_cliente_por_celular(celular_buscar)
    print('lineaa 101', cliente_encontrado)

    if cliente_encontrado:
      print("Cliente encontrado:")
      print(cliente_encontrado)
    else:
      print("Cliente no encontrado.")
  ################################# AGREGADO 5 ⬆️ #################################

  elif opcion == "4":
    # Salir
    print("Saliendo del programa.")
    break

  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")