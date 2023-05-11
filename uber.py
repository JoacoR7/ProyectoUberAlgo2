def menu():
    opcion = 0
    while opcion != 9:
        print(" 1: Mostrar los usuarios\n", 
            "2: Mostrar los autos\n",
            "3: Mostrar los lugares\n",
            "4: Mostrar las esquinas\n"
            " 5: Crear un usuario\n",
            "6: Crear un auto\n",
            "9: Salir")
        
        opcion = input()
        try:
            opcion = int(opcion)
        except ValueError:
            pass
        finally:
            opcion = opcion


        if opcion == 1:
            print("Personas")
        elif opcion == 2:
            print("Autos")
        elif opcion == 9:
            print("¡Nos vemos!")
        else:
            print("Opción inválida, por favor intente de nuevo, recuerde ingresar un número del 1 al 9")
        
