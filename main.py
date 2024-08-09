import json
import modules.funcionGlobal as fg
import modules.corefiles as cf
import ui.menus as ui

def main():
    fg.borrar_pantalla()
    cf.iniciarRegistroTransacciones()
    while True:
        opcion = ui.MenuPrincipal()
        if opcion == 4:
            break

if __name__ == '__main__':
    main()
