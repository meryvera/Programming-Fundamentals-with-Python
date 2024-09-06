# CALCULO DE INDICE DE MASA CORPORAL - IMC

# Declaracion y Asignacion de valores a las variables con la entrada de datos
var_peso = float(input("Ingresa tu peso en kilogramos: "));
var_altura = float(input("Ingresa tu altura en metros: "));

# Procesamos los datos
IMC = var_peso / (var_altura **2);

# mostramos la salida de los datos procesaos
print("Tu IMC es: ", IMC);


