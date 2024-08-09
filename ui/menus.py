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

def tittleVentas():
    tittleV = """
********************************
*            VENTAS            *
*            PanCamp           *
********************************
"""
    print(tittleV)

def tittleCompras():
    tittleC = """
********************************
*            COMPRAS           *
*            PanCamp           *
********************************
"""
    print(tittleC)

def tittleInformes():
    tittleInfor = """
********************************
*           INFORMES           *
*           PanCamp            *
********************************
"""
    print(tittleInfor)

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

def MenuInformes():
    fg.borrar_pantalla()
    tittleInformes()
    menu_informes = """1. Generar Informe de Ventas \n2. Generar informe de Compras """
    print(menu_informes)
    print(" ")
    
    try:
        op = int(input("Ingrese la opción: "))
        if op == 1:
            fg.borrar_pantalla()
            tittleVentas()
            fecha_inicio_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin_str = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            fg.borrar_pantalla()
            rep.generar_informe_ventas(fecha_inicio_str, fecha_fin_str)
        elif op == 2:
            fecha_inicio_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin_str = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            fg.borrar_pantalla()
            rep.generar_informe_compras(fecha_inicio_str, fecha_fin_str)
        
        elif op == 3:
            return 3
        else:
            print("Opción no válida")
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
            fg.borrar_pantalla()
            tittleVentas()
            aggtran.añadirTransaccion()
        elif op == 2:
            fg.borrar_pantalla()
            tittleCompras()
            aggCom.añadirCompra()
        elif op == 3:
            fg.borrar_pantalla()
            tittleInformes()
            MenuInformes()
        elif op == 4:
            return 4
        else:
            print("Opción no válida")
    except ValueError:
        print("Ingrese una opción correcta")
    fg.pausar_pantalla()
    return None
