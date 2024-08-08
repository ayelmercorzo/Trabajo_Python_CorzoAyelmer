import json
import ui.uiMenuPrincipal as uiM
import modules.funcionGlobal as fg

def añadirTransaccion():
    fecha= input("Ingrese la fecha de la transaccion: ")
    nombreCliente = input ("Ingrese el nombre del cliente: ")
    direccionCliente = input ("Ingrese la direccion del cliente: ")
    empleado = input ("Ingrese nombre del empleado y su cargo (separado por un espacio): ")
    cargo = input ("Ingrese su cargo: ")
    producto = input ("Ingrese el nombre del producto: ")
    cantidad = input ("Ingrese la cantidad vendida: ")
    precio = input ("Ingrese el precio: ")

    transaccion = {
        'Fecha de la transaccion': fecha,
        'Nombre del cliente': nombreCliente,
        'Direccion del cliente': direccionCliente,
        'Empleado': empleado,
        'Cargo': cargo,
        'Producto': producto,
        'Cantidad': cantidad,
        'Precio': precio 
    }

    aggDataTransaccion('transaccion', transaccion, producto)
    print("¡Transaccion EXITOSA!")
    fg.pausar_pantalla()
    uiM.mainMenu("op")

def aggDataTransaccion(namespace,transaccion, producto):
    try:
        with open('data/medicos.json', 'r+') as file:
            data_transaccion = json.load(file)
    except FileNotFoundError:
        data_transaccion = {namespace: {}}

    data_transaccion[namespace][producto].append(transaccion)

    with open('data/medicos.json', 'w') as file:
        json.dump(data_transaccion, file, indent=4)