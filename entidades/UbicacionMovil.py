class UbicacionMovil:
	nombre = None
	direccion = None
	monto = None

	def __init__(self, nombre, direccion, monto):
		self.nombre = nombre
		self.direccion = direccion
		self.monto = monto

	def getNombre(self):
		return self.nombre

	def setNombre(self,nombre):
		self.nombre = nombre

	def getDireccion(self):
		return self.direccion  

	def setDireccion(self,direccion):
		self.direccion = direccion

	def getMonto(self):
		return self.monto  

	def setMonto(self,monto):
		self.monto = monto
