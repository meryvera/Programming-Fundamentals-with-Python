# RECORRIDO DE DICCIONARIOS - FOR IN

# Definir una lista de diccionarios
personas = [
  {'nombre': 'Juan', 'edad': 28},
  {'nombre': 'María', 'edad': 34},
  {'nombre': 'Pedro', 'edad': 40},
  {'nombre': 'Ana', 'edad': 22}
]

# Usar un bucle for para iterar sobre la lista de diccionarios
for persona in personas:
  # print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
  print("Nombre:", persona['nombre'], "Edad:", persona['edad'])

