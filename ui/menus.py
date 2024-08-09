import modules.funcionGlobal as fg
import modules.aggTransaccion as aggtran
import modules.aggCompra as aggCom
import modules.reportes as rep

def tituloBienvenida():
    title = """
********************************
*   BIENVENIDO A LA PANADERIA  *
*          PanCamp             *
********************************
    """
    print(title)

def MenuCompra():
    menu_compra = """1. Panaderia \n2. Pasteleria \n3. Bebidas \n4. Promociones"""
    print(menu_compra)
    print(" ")
    try:
        op = int(input("Ingrese la opción: "))
        if op not in [1, 2, 3, 4]:
            print("Opción no válida")
            return None
        return op
    except ValueError:
        print("Ingrese una opción correcta")
        fg.pausar_pantalla()
        return None

def MenuPrincipal():
    fg.borrar_pantalla()
    tituloBienvenida()
    tittle_menu_principal = """1. Venta \n2. Compra \n3. Generar Informes \n4. Salir"""
    print(tittle_menu_principal)
    print(" ")
    try:
        op = int(input("Ingrese la opción: "))
        if op == 1:
            aggtran.añadirTransaccion()
        elif op == 2:
            aggCom.añadirCompra()
        elif op == 3:
            rep.generarInformes()
        elif op == 4:
            return 4
        else:
            print("Opción no válida")
    except ValueError:
        print("Ingrese una opción correcta")
    fg.pausar_pantalla()
    return None
