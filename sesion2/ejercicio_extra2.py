# PROCESO DE VENTA DE SOFTWARES

# Entrada de datos
cantidad = int(input("Ingrese la cantidad de licencias de software que desea comprar: "))

# Inicialización de variables
precio_unitario = 100
descuento = 0

# Cálculo del subtotal
subtotal = cantidad * precio_unitario

# Aplicación de descuentos si corresponde
if cantidad > 10:
  descuento = subtotal * 0.1

# Cálculo de subtotal con descuento
subtotal = subtotal - descuento

# Cálculo de impuestos
impuesto = subtotal * 0.15

# Cálculo del total
total = subtotal + impuesto

# Salida de resultados
print("Subtotal (sin descuento): $", cantidad * precio_unitario)
print("Descuento aplicado: $", descuento)
print("Subtotal (con descuento): $", subtotal)
print("Impuesto (15%): $", impuesto)
print("Total a pagar: $", total)
