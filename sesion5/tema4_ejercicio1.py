# SCOPE GLOBAL Y LOCAL

# Variable Global
numeroGlobal = 10

def  mostrarVariableLocal( ):
  global numeroGlobal
  # Variable Local
  numeroLocal = 5;
  print("Número Local desde dentro de la funcion: ", numeroLocal);
  print("Número Global desde dentro de la funcion: ", numeroGlobal);
  numeroGlobal = 25;
      
mostrarVariableLocal()
print("Número Global desde fuera de la funcion, con nuevo valor: ", numeroGlobal) # 10

# print("Número Global después de llamar a la función: ", numeroGlobal) # 25