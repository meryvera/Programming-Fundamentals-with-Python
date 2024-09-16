# AGREGAR ALGORITMO DE BUSQUEDA

clientes = [
  {'nombre': 'Adri', 'email': 'adri@hola.com', 'celular': 987654321},
  {'nombre': 'Jose', 'email': 'jose@hola.com', 'celular': 999999999},
  {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},
  {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567}
]

################################# AGREGADO 4 ⬇️ #################################
# Ordena la lista de clientes por número de celular.
clientes.sort(key = lambda cadaElemento: cadaElemento['celular'])
print('clientes ordenados', clientes)
# clientes = [
#   {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},
#   {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567}
#   {'nombre': 'Adri', 'email': 'adri@hola.com', 'celular': 987654321},
#   {'nombre': 'Jose', 'email': 'jose@hola.com', 'celular': 999999999},
# ]

# Busca un cliente por número de celular usando búsqueda binaria
izquierda = 0
derecha = len(clientes) - 1 # 4-1
print('indice de la derecha', derecha) # 3

while izquierda <= derecha:
  # Condición del bucle: El bucle while continúa ejecutándose mientras izquierda sea menor o igual a derecha. 
  # Esto significa que hay un rango válido en el que buscar.

  medio = (izquierda + derecha) // 2   # 1
  # Cálculo del índice medio: Calcula el índice medio del rango actual sumando izquierda y derecha
  #  y dividiendo el resultado entre 2, usando la división entera (//) para obtener un número entero.
  # Este índice se usa para dividir el rango en dos mitades.

  print('indice del medioo', medio) # 1   # 0 # Devuelve el índice del cliente
  cliente_medio = clientes[medio]
  print('cliente de en medio', cliente_medio)
  # {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567}
  # {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},

  if cliente_medio["celular"] == 911144567:
    print(cliente_medio)
    print(medio) # Devuelve el índice del cliente
  elif cliente_medio["celular"] < 911144567:
    izquierda = medio + 1
  else:
    derecha = medio - 1

################################# AGREGADO 4 ⬇️ #################################