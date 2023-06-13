import sys
import servicios.UbicacionMovilServicio as um
import servicios.UbicacionFijaServicio as uf
import servicios.MapaServicio as ms

if __name__ == "__main__":
    args = sys.argv
    command = args[1]
    if command == "-load_movil_element":
        um.load_movil_element(args[2], args[3], args[4])
    elif command == "-load_fix_element":
        uf.load_fix_element(args[2], args[3])
    elif command == "-create_trip":
        pass
    elif command == "-create_map":
        ms.crearMapa(args[2])
