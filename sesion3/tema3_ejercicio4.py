# MANIPULACION DE PILAS

# Definir una pila
pila = []

# Operaciones append
pila.append(1)  # Añadir 1 a la pila
pila.append(2)  # Añadir 2 a la pila
pila.append(3)  # Añadir 3 a la pila
print(pila)     # Imprime [1, 2, 3]

# Operación peek
top = pila[-1]  # Ver el último elemento (cima de la pila) sin eliminarlo
print(top)      # Imprime 3

# Operaciones pop
elemento = pila.pop()  # Eliminar y devolver el último elemento
print(elemento)        # Imprime 3
print(pila)            # Imprime [1, 2]

# Intentar pop en una pila vacía
pila.pop();
pila.pop();

pila.append(8)
pila.append(13)

if len(pila) != 0:
  pila.pop()
else:
  print("La pila está vacía.")  # Imprime "La pila está vacía."
