class GestorClientes:
  def __init__(self):
    self.clientes = [
      {'nombre': 'Adri', 'email': 'adri@hola.com', 'celular': 987654321},
      {'nombre': 'Jose', 'email': 'jose@hola.com', 'celular': 999999999},
      {'nombre': 'Isa', 'email': 'isa@hola.com', 'celular': 911144567},
      {'nombre': 'Isra', 'email': 'isra@hola.com', 'celular': 922244567}
    ]

  # Funcion ordenar clientes
  def ordenar_clientes(self):
    # Ordena la lista de clientes por número de celular
    self.clientes.sort(key=lambda x: x["celular"])

  # Funcion buscar cliente
  def buscar_cliente_por_celular(self, celular_buscar):
    #Busca un cliente por número de celular usando búsqueda binaria
    izquierda = 0
    derecha = len(self.clientes) - 1

    while izquierda <= derecha:
      medio = (izquierda + derecha) // 2
      cliente_medio = self.clientes[medio]

      if cliente_medio["celular"] == celular_buscar:
        print(cliente_medio)
        return medio # Devuelve el índice del cliente
      elif cliente_medio["celular"] < celular_buscar:
        izquierda = medio + 1
      else:
        derecha = medio - 1

    return None
  
  # Funcion guardar cliente nuevo
  def agregar_cliente(self, nombre, email, celular):
    # Agrega un nuevo cliente a la lista
    datos_validos = True

    if len(nombre) == 0:
      datos_validos = False

    if '@' not in email or '.' not in email:
      datos_validos = False

    if len(celular) != 9 or not celular.isdigit():
      datos_validos = False

    if datos_validos:
      cliente = {
        "nombre": nombre,
        "email": email,
        "celular": int(celular)
      }
      self.clientes.append(cliente)
      self.ordenar_clientes()
      print("Cliente agregado exitosamente")
    else:
      print("Datos inválidos. Vuelve a ingresar los datos.")

  def eliminar_cliente(self, celular):
    # Elimina un cliente por número de celular
    indice_cliente = self.buscar_cliente_por_celular(celular)
    if indice_cliente is not None:
      del self.clientes[indice_cliente]
      print("Cliente eliminado exitosamente")
    else:
      print("Cliente no encontrado.")

  def mostrar_clientes(self):
    # Muestra todos los clientes guardados
    if self.clientes:
      print("clientes guardados:")
      for cliente in self.clientes:
        print(cliente)
    else:
      print("No hay clientes para mostrar.")

def main():
  gestor = GestorClientes()

  while True:
    print("Opciones:")
    print("1. Agregar un cliente nuevo")
    print("2. Mostrar todos los clientes")
    print("3. Buscar un cliente por celular")
    print("4. Eliminar un cliente por celular")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
      nombre = input("Ingrese el nombre: ")
      email = input("Ingrese el e-mail: ")
      celular = input("Ingrese el celular: ")
      gestor.agregar_cliente(nombre, email, celular)

    elif opcion == "2":
      gestor.mostrar_clientes()

    elif opcion == "3":
      celular_buscar = int(input("Ingrese el número de celular del usuario a buscar: "))
      cliente_encontrado = gestor.buscar_cliente_por_celular(celular_buscar)
      
      if cliente_encontrado is not None:
        print("Cliente encontrado:")
        print(gestor.clientes[cliente_encontrado])
      else:
          print("Cliente no encontrado.")

    elif opcion == "4":
      celular_eliminar = int(input("Ingrese el número de celular del usuario a eliminar: "))
      gestor.eliminar_cliente(celular_eliminar)

    elif opcion == "5":
      print("Saliendo del programa.")
      break

    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
  main()