import sys
import servicios.UbicacionMovilServicio as um
import servicios.UbicacionFijaServicio as uf
import servicios.MapaServicio as ms

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("Comandos: -h, -help, -load_movil_element, -load_fix_element, -create_trip, -create_map")
    else:
        command = args[1]
        if command == "-load_movil_element":
            um.load_movil_element(args[2], args[3], args[4])
        elif command == "-load_fix_element":
            uf.load_fix_element(args[2], args[3])
        elif command == "-create_trip":
            pass
        elif command == "-create_map":
            ms.crearMapa(args[2])
        elif command == "-h" or command == "-help":
            print("-load_movil_element: carga de ubicacion móvil")
            print("-load_fix_element: carga de ubicación fija")
            print("-create_trip: realizar viaje hacia alguna dirección")
            print("-create_map: ingresar mapa")
        else:
            print('Ingrese el comando "-h" o "-help" para más información')
