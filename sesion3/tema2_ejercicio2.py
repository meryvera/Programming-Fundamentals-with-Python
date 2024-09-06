# RECORRIDO DE DICCIONARIOS - WHILE

# Definir una lista de diccionarios
personas = [
  {'nombre': 'Juan', 'edad': 28},
  {'nombre': 'María', 'edad': 34},
  {'nombre': 'Pedro', 'edad': 40},
  {'nombre': 'Ana', 'edad': 22}
]

# Aunque no es tan común como for, también puedes usar while para recorrer la lista de diccionarios:

# Usar un bucle while para iterar sobre la lista de diccionarios
i = 0
while i < len(personas):
  persona = personas[i]
  print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
  i = i + 1
  # i += 1

