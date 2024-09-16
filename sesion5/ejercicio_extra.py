# CUENTA REGRESIVA CON FUNCION REGRESIVA
def cuenta_regresiva_recursiva(n):
  if n < 0:
    print("Despegue con recursion!")
  else:
    print(n)
    cuenta_regresiva_recursiva(n-1)

# Llamada a la funcion con un numero inciial
cuenta_regresiva_recursiva(5)


# CUENTA REGRESIVA SIN FUNCION REGRESIVA PERO CON WHILE
def cuenta_regresiva_while(n):
  while n >= 0:
    print(n)
    n = n-1

  print('Despegue con while!!')

cuenta_regresiva_while(5)