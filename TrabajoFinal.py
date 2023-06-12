print("Bienvenidos Al poder juducial Cordoba")
print("1.Consulta de ley por numero: ")
print("2.Consulta de ley por palabra: ")
print("3.Modificar una ley:")
print("4.Salir")

eleccion = int(input("Por favor ingrese una opcion: "))

match eleccion:
    case 1:
        print("Usted a seleccionado Consulta de ley por numero")
    case 2: 
        print("Usted a seleccionado Consulta de ley por palabra")
    case 3:
        print("Usted a seleccionado Modificar una ley")
    case 4:
        print("Usted a seleccionado salir")
    case _:
        print("Ha seleccionado una opcion incorrecta")                