from os import system
import sys

CMCAL = {
  "data": {}
}


def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def pausar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar")
  else:
    system("pause")

def salir():
    print("Estas saliendo del programa...")
    sys.exit()