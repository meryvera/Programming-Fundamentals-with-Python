# CREAMOS LA CLASE USUARIO CON SUS METODOS Y PROPIEDADES
class Usuario:
  def __init__(self, nombre, apellido, email, password):
    self.nombre = nombre;
    self.apellido = apellido;
    self.email = email;
    self.password = password;

  def editarPerfil(self):
    print('Puedes editar los datos de tu perfil,' , self.nombre, 'y', self.apellido);

  def editarPassword(self):
    print('Puedes editar tu password:', self.password)

# INSTANCIAMOS 1 OBJETO PARTIENDO DESDE EL MOLDE O CLASE USUARIO
persona1 = Usuario('Adriana', 'Salas', 'adri@hola', 123)
persona2 = Usuario('Isabel', 'Garcia', 'isa@hola', 567)
persona3 = Usuario('Nico', 'Sanchez', 'nico@hola', 678)

print(persona1)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.editarPassword())

print(persona2.nombre)
print(persona3.nombre)
