import uber
import servicios.serializacion
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um

#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))


um.load_movil_element(nombre,direccion)
uf.load_fix_element(nombre,direccion)

#uber.menu()

