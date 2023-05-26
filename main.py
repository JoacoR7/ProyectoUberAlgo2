import uber
import servicios.serializacion
import servicios.MapaServicio as ms

#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print("a")


#uber.menu()