class Persona:
    nombre = None
    apellido = None
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def getNombre(self):
          return self.nombre
    
    def getApellido(self):
         return self.apellido
    
    def setNombre(self,nombre):
         self.nombre = nombre
         
    def setApellido(self,apellido):
          self.apellido = apellido