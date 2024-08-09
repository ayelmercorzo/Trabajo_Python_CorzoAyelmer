import json
import ui.menus as uiM
import modules.funcionGlobal as fg

def mostrarStock(categoria):
    try:
        with open('json/data.json', 'r') as file:
            data = json.load(file)
            productos = data.get(categoria, {})
            
            if not productos:
                print(f"No hay productos disponibles en la categoría '{categoria}'.")
                return
            
            print(f"Productos en stock para '{categoria}':")
            for producto, precio in productos.items():
                print(f"{producto}: Precio: {precio}")
    except FileNotFoundError:
        print("No se encontró el archivo de datos de productos.")
    except Exception as e:
        print(f"Error al mostrar el stock: {e}")

def añadirTransaccion():
    fecha = input("Ingrese la fecha de la transacción (YYYY-MM-DD): ")
    nombreCliente = input("Ingrese el nombre del cliente: ")
    direccionCliente = input("Ingrese la dirección del cliente: ")
    empleado = input("Ingrese nombre del empleado: ")
    cargo = input("Ingrese su cargo: ")
    categorias = {
        '1': 'Panaderia',
        '2': 'Pasteleria',
        '3': 'Bebidas',
        '4': 'Promociones'
    }
    fg.borrar_pantalla()
    print("Seleccione el tipo de producto:")
    for clave, categoria in categorias.items():
        print(f"{clave}. {categoria}")

    while True:
        op_categoria = input("Ingrese la opción de categoría: ")
        categoria = categorias.get(op_categoria)
        if categoria:
            mostrarStock(categoria)
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    productos = []
    
    while True:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad vendida: ")
        precio = input("Ingrese el precio: ")

        producto_info = {
            'Producto': producto,
            'Cantidad': cantidad,
            'Precio': precio
        }

        productos.append(producto_info)

        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

    transaccion = {
        'Fecha de la transacción': fecha,
        'Nombre del cliente': nombreCliente,
        'Dirección del cliente': direccionCliente,
        'Empleado': empleado,
        'Cargo': cargo,
        'Productos': productos
    }

    aggDataTransaccion('transacciones', transaccion)
    print("¡Transacción EXITOSA!")
    fg.pausar_pantalla()
    uiM.MenuPrincipal()

def aggDataTransaccion(namespace, transaccion):
    try:
        with open('data/transacciones.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if namespace not in data or not isinstance(data[namespace], list):
        data[namespace] = []

    data[namespace].append(transaccion)

    with open('data/transacciones.json', 'w') as file:
        json.dump(data, file, indent=4)
