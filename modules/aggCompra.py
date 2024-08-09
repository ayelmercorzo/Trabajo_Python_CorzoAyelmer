import json
import ui.menus as uiM
import modules.funcionGlobal as fg

def añadirCompra():
    fecha = input("Ingrese la fecha de la Compra (YYYY-MM-DD): ")
    nombreProvedor = input("Ingrese el nombre del Proveedor: ")
    contactoProvedor = input("Ingrese el contacto del Proveedor: ")
    productos = []

    while True:
        productoComprado = input("Ingrese nombre del Producto comprado: ")
        productoCantidad = input("Ingrese la cantidad de Productos: ")
        productoPrecio = input("Ingrese el precio del Producto: ")

        producto_info = {
            'Producto': productoComprado,
            'Cantidad': productoCantidad,
            'Precio': productoPrecio
        }
        productos.append(producto_info)

        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

    compra = {
        'Fecha de la compra': fecha,
        'Informacion del Proveedor': {
            'Nombre': nombreProvedor,
            'Contacto': contactoProvedor
        },
        'Productos': productos
    }

    aggDataCompra('compras', compra)
    print("¡Compra EXITOSA!")
    fg.pausar_pantalla()
    uiM.MenuPrincipal()

def aggDataCompra(namespace, compra):
    try:
        with open('data/compras.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if namespace not in data or not isinstance(data[namespace], list):
        data[namespace] = []

    data[namespace].append(compra)

    with open('data/compras.json', 'w') as file:
        json.dump(data, file, indent=4)
