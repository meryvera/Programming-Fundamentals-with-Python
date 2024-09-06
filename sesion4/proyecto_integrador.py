# AGREGAR ALGORITMO DE BUSQUEDA

clientes = [
  {'nombre': 'Adri', 'email': 'adri@hola.com', 'celular': 987654321},
  {'nombre': 'Jose', 'email': 'jose@hola.com', 'celular': 999999999},
  {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},
  {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567}
]

################################# AGREGADO 4 ⬇️ #################################
# Ordena la lista de clientes por número de celular.
clientes.sort(key = lambda x: x['celular'])
print('ahh', clientes)


# Busca un cliente por número de celular usando búsqueda binaria
izquierda = 0
derecha = len(clientes) - 1 # 4-1
print('derechaaa', derecha)

while izquierda <= derecha:
  medio = (izquierda + derecha) // 2
  cliente_medio = clientes[medio]

  if cliente_medio["celular"] == 911144567:
    print(cliente_medio)
    print(medio) # Devuelve el índice del cliente
  elif cliente_medio["celular"] < 911144567:
    izquierda = medio + 1
  else:
    derecha = medio - 1
################################# AGREGADO 4 ⬇️ #################################