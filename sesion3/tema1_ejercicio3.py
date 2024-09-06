# RECORRIDO DE LISTAS - WHILE

# Declaramos Y asignamos una lista de valores
numeros = [1,2,3,4,5]

# Inicializamos la variable indice
indice = 0

# Usamos un bucle while para recorrer la lista
while indice < len(numeros):
  print('este el elemento', numeros[indice], 'de la lista')
  indice = indice + 1
  # indice += 1