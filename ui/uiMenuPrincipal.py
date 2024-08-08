import modules.funcionGlobal as fg
import ui.menu as menu
import modules.aggTransaccion as aggtran

def mainMenu(op : int):
    fg.borrar_pantalla()
    menu.tituloBienvenida()
    menuPrincipal = """1. Venta \n2. Compra \n3. Generar Informes"""

    if (op != 4):
        
        print(menuPrincipal)
        print(" ")
        try:
            op = int(input("Ingrese la opcion: "))
        except ValueError:
                print("Ingrese una opcion correcta")
                fg.pausar_pantalla()
                mainMenu(0)
        else:
            match op:
                case 1:
                    aggtran.añadirTransaccion()
                case 2:
                    print("Error Ingrese otra opcion")
                case 3:
                    print("Error Ingrese otra opcion")
                    
        
                