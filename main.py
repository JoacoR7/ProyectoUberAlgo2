import uber
import servicios.serializacion
import servicios.MapaServicio as ms
<<<<<<< HEAD
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
=======
import entidades.graph as g
>>>>>>> 6adba57ed0525578bd5bc028f21881ef088196e8

cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))

<<<<<<< HEAD

um.load_movil_element(nombre,direccion)
uf.load_fix_element(nombre,direccion)

#uber.menu()

=======
g.shortestPath(map, 7, 4)
print("")

ms.cálculosIniciales(map)

#TODO: arreglar inserción de grafo, aunque no salgan aristas de un vértice, colocar datos en el slot correspondiente (al menos la key)
>>>>>>> 6adba57ed0525578bd5bc028f21881ef088196e8
