# RECORRIDO DE LISTAS - FOR IN RANGE

# Declaramos e inicializamos la variable var_arreglo con 4 elementos
var_lista = [4, 7, 11, 21]

# Iteramos sobre cada elemento en var_lista
for i in range(len(var_lista)):
  # Si el valor del elemento es menor o igual a 10, incrementamos en +3
  if var_lista[i] <= 10:
    # var_lista[i] += 3
    var_lista[i] = var_lista[i] + 3
    # print(f"El valor del arreglo en la posición {i+1}, es ahora {var_lista[i]}")
    print("El valor del arreglo en la posición", i+1, "es ahora " , var_lista[i])
  else:
    # print(f"El valor del arreglo en la posición {i+1}, no cumple con la condición")
    print("El valor del arreglo en la posición", i+1, "no cumple con la condición")

print("El bucle ya se detuvo")
