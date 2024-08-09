from os import system
import sys

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presione una tecla para continuar")
    else:
        system("pause")

def salir():
    print("Estás saliendo del programa...")
    sys.exit()
