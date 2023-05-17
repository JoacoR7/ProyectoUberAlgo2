class UbicacionFija:
    nombre = None
    direccion = None

    def __init__(self, nombre, direccion):
        self.nombre =  nombre
        self.direccion = direccion

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion