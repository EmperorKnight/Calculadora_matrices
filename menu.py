import sistema_pivote
import sistemas
import os

def menu():
    print("1 = Resolver sistemas \n2 = Conocer pivote de un sistema \n3 = Salir")

def limpiar():
    os.system("cls || clear")

def realizar():
    limpiar()
    menu()
    eleccion = input("Ingrese su decision: ")
    
    if eleccion == '1':
        limpiar()
        sistemas.main()
    elif eleccion == '2':
        limpiar()
        sistema_pivote
    elif eleccion == '3':
        limpiar()
        exit("Salida del sistema con exito...\n")
    else:
        input("Perdone, no disponemos de esta eleccion, persione enter para continuar . . . ")
        realizar()

def main():
    limpiar()
    realizar()

main()