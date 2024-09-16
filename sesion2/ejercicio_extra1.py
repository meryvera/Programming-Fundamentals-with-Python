# PROCESO DE DEVOLUCION DE PRODUCTO DEFECTUOSO

# Entrada de datos
var_entrada_defectuoso = input("¿El producto está defectuoso? (si/no): ")

if var_entrada_defectuoso == "si":
    es_defectuoso = True
else:
    es_defectuoso = False

if es_defectuoso:
  var_entrada_garantia = input("¿El producto tiene garantía? (si/no): ")

  if var_entrada_garantia == "si":
    tiene_garantia = True
  else:
    tiene_garantia = False

  if tiene_garantia:
    print("Procesar devolución y reembolsar dinero.")
  else:
    print("La garantía ha expirado. No se puede proceder con la devolución.")

else:
  print("El producto no está defectuoso. No aplica devolución.")
