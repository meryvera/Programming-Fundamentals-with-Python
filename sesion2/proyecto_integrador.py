# Ingresar nombre, e-mail, teléfono
nombre = input("Ingrese el nombre: ")
email = input("Ingrese el e-mail: ")
celular = input("Ingrese el celular: ")

# Validamos los datos (formato e-mail, campos obligatorios)
datos_validos = True

# Decisión basada en la validez de los datos
if datos_validos:
  # Registramos cliente
  print("Cliente agregado exitosamente")
else:
  # Datos inválidos
  print("Datos inválidos. Vuelve a ingresar los datos.")

