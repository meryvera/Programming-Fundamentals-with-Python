class Cliente:
    def __init__(self, nombre, email, celular):
        self.nombre = nombre
        self.email = email
        self.celular = celular
    
    def __repr__(self):
        return f'Cliente (nombre={self.nombre}, email={self.email}, celular={self.celular})'
        
# nuevoCliente = Cliente('mario', 'mario@hola.com', 987654321)
# print('este es el valor del nuevo cliente', nuevoCliente)
# print(f'este es el valor del nuevo cliente: {nuevoCliente}')

class ClientesCRM:
    def __init__(self):
        self.clientes = [
            Cliente('Adri', 'adri@hola.com', 987654321),
            Cliente('Jose', 'jose@hola.com', 999999999),
            Cliente('Isa', 'isa@hola.com', 911144567),
            Cliente('Isra', 'isra@hola.com', 922244567),
        ]
     
    # Definir funcion de ordenamiento de clientes
    def ordenar_clientes(self):
        # Ordena la lista de clientes por número de celular
        self.clientes.sort(key=lambda cadaElemento: cadaElemento.celular)
    
    # definir funcion de busqueda binaria
    def buscar_cliente_por_celular(self, celular_buscar):
      self.ordenar_clientes()
      #Busca un cliente por número de celular usando búsqueda binaria
      izquierda = 0
      derecha = len(self.clientes) - 1
    
      while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        cliente_medio = self.clientes[medio]
    
        if cliente_medio.celular == celular_buscar:
          print('Se encontro al cliente buscado')
          return cliente_medio # Devuelve el índice del cliente
        elif cliente_medio.celular < celular_buscar:
          izquierda = medio + 1
          print('el universo esta hacia la derecha')
        else:
          derecha = medio - 1
          print('el universo esta hacia la izquierda')       
     
    # definir funcion de mostrar clientes existentes   
    def mostrar_clientes(self):
        self.ordenar_clientes()
        print("Clientes guardados:")
        for cadaCliente in self.clientes:
          print(cadaCliente)

    # definir funcion de agregar clientes nuevos
    def agregar_cliente(self, nombre, email, celular):
        # Validamos los datos (formato e-mail, campos obligatorios)
        datos_validos = True
    
        # Verificar que el nombre no esté vacío
        if len(nombre) == 0:
          datos_validos = False
    
        # Verificar que el e-mail contenga '@' y '.'
        if '@' not in email or '.' not in email:
          datos_validos = False
    
        # Verificar que el teléfono tenga 9 dígitos
        if len(celular) != 9:
          datos_validos = False
    
        if datos_validos:
            nuevo_cliente = Cliente(nombre, email, int(celular))
            self.clientes.append(nuevo_cliente)
            self.ordenar_clientes()
            print("Cliente agregado exitosamente")
        else:
           # Datos inválidos
           print("Los datos son inválidos. Vuelve a ingresar los datos.")
    
    # definir funcion de aliminar cliente existente
    def eliminar_cliente_por_celular(self, celular_eliminar):
        cliente_encontrado = self.buscar_cliente_por_celular(celular_eliminar)
        
        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            print(f"Cliente con celular {cliente_encontrado.celular} ha sido eliminado")
        else:
            print(f"No se encontro ningun cliente con el numero de celular")
        
def main():
    crm = ClientesCRM()
    while True:
        print("Opciones:")
        print("1. Agregar un cliente nuevo")
        print("2. Mostrar todos los clientes")
        print("3. Buscar un cliente por celular") # AGREGADO 5 ⬆️
        print("4. Eliminar un cliente por celular")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4): ")
    
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el e-mail: ")
            celular = input("Ingrese el celular: ")
            
            crm.agregar_cliente(nombre, email, celular)
            
        elif opcion == "2":
            crm.mostrar_clientes()
            
        elif opcion == "3":
            # Buscar un usuario por número de celular 
            celular_buscar = int(input("Ingrese el número de celular del cliente a buscar: "))
            
            cliente_encontrado = crm.buscar_cliente_por_celular(celular_buscar)
            
            if cliente_encontrado:
                print("Cliente encontrado: ", cliente_encontrado)
            else:
                print("El cliente no existe en la base de datos")
        
        elif opcion == "4":
            celular_buscar = int(input("Ingrese el numero de celular del cliente a liminar"))
            crm.eliminar_cliente_por_celular(celular_buscar)
            
        elif opcion == "5":
            # Salir
            print("Se escogio salir del programa")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            
main()

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    