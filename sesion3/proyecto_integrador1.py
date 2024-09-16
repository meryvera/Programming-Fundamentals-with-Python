# AGREGAR CLIENTE CON VALIDACIONES

# Ingresar nombre, e-mail, teléfono
nombre = input("Ingrese el nombre: ")
email = input("Ingrese el e-mail: ")
celular = input("Ingrese el celular: ")

# AGREGAMOS VALIDACIONES 
##################################################################
# Validamos los datos (formato e-mail, campos obligatorios)
datos_validos = True

# Verificar que el nombre no esté vacío
if len(nombre) <= 2:
  datos_validos = False

# Verificar que el e-mail contenga '@' y '.'
if '@' not in email or '.' not in email:
  datos_validos = False

# Verificar que el teléfono tenga 9 dígitos
if len(celular) != 9:
  datos_validos = False
##################################################################

# Decisión basada en la validez de los datos
if datos_validos:
  # Registramos cliente
  print("Cliente agregado exitosamente")
else:
  # Datos inválidos
  print("Los datos son inválidos. Vuelve a ingresar los datos.")


