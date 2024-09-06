# VENTA DE VEHICULOS

# Clase Padre "Vehiculo"
class Vehiculo:
  def __init__(self, nombre, marca, año):
    self.nombre = nombre
    self.marca = marca
    self.año = año

  def encender(self):
    print("El", self.nombre, "está encendido.")

  def apagar(self):
    print("El", self.nombre, "está apagado.")


# Clase Hija "Auto" que hereda de Vehículo
class Auto(Vehiculo):
  def __init__(self, nombre, marca, año, descapotable):
    super().__init__(nombre, marca, año)
    self.descapotable = descapotable
  
  def mostrar_tipo(self):
      print(f"El auto {self.nombre} es {'descapotable' if self.descapotable else 'no descapotable'}.")


# Clase Hija "Moto" que hereda de Vehículo
class Moto(Vehiculo):
  def __init__(self, nombre, marca, año, tipoManilla):
    super().__init__(nombre, marca, año)
    self.tipoManilla = tipoManilla

  def mostrar_tipo(self):
    print(f"La moto {self.nombre} tiene una manilla de tipo {self.tipoManilla}.")


# Instanciando objetos
auto1 = Auto("Civic", "Honda", 2021, True)
moto1 = Moto("Ninja", "Kawasaki", 2021, "Deportivo")

# Usando métodos de los objetos
auto1.encender()
auto1.mostrar_tipo()
moto1.encender()
moto1.mostrar_tipo()
