import uber
import entidades.dictionary as d
import servicios.serializacion as s
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
import entidades.graph as g
import servicios.UbicacionFijaServicio as uf
#servicios.serializacion.serializarPersonas(["A", "B", "C"])
from entidades.borrar import *

um.load_movil_element("P1", "<e8,10> <e10,40>", "2000")
