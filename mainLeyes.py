import os             
from os import system
from sqlite3 import connect
import time 
import funciones
os.system
       
while True:
    menu= """
    =========================================
    Bienvenidos Al Poder Judicial Córdoba
    =========================================
    [1]--> Insertar una nueva ley
    [2]--> Modificar ley
    [3]--> Eliminar ley
    [4]--> Buscar ley por número
    [5]--> Buscar ley por palabra clave
    [6]--> Salir
    =========================================
    """
    print (menu)

    try:
        opcion= int(input("Seleccione la opcion deseada: "))
        if(opcion == 1):
            print("Usted a seleccionado insertar una nueva Ley")
            funciones.Leyes.insertar_nueva_ley()
            time.sleep(2)
            os.system('cls')
}
