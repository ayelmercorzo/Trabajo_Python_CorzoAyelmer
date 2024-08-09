import json
from datetime import datetime

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def generar_informe_ventas(fecha_inicio_str, fecha_fin_str):
    if not (validar_fecha(fecha_inicio_str) and validar_fecha(fecha_fin_str)):
        print("Error: Las fechas deben estar en el formato 'YYYY-MM-DD' y ser válidas.")
        return

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
        
        if fecha_inicio > fecha_fin:
            print("Error: La fecha de inicio debe ser anterior a la fecha de fin.")
            return
        
        with open('data/transacciones.json', 'r') as file:
            data = json.load(file)
        
        ventas = data.get('transacciones', [])
        total_ingresos = 0

        print(f"Informe de Ventas desde {fecha_inicio_str} hasta {fecha_fin_str}:")
        for transaccion in ventas:
            fecha_transaccion = datetime.strptime(transaccion['Fecha de la transacción'], '%Y-%m-%d')
            if fecha_inicio <= fecha_transaccion <= fecha_fin:
                print(f"Fecha: {transaccion['Fecha de la transacción']}")
                print(f"Cliente: {transaccion['Nombre del cliente']}")
                print(f"Dirección: {transaccion['Dirección del cliente']}")
                print(f"Empleado: {transaccion['Empleado']}")
                print(f"Cargo: {transaccion['Cargo']}")
                print("Productos vendidos:")
                for producto in transaccion['Productos']:
                    print(f"  Producto: {producto['Producto']}, Cantidad: {producto['Cantidad']}, Precio: {producto['Precio']}")
                    total_ingresos += float(producto['Precio']) * float(producto['Cantidad'])
                print()

        print(f"Total de ingresos en el período: {total_ingresos}")

    except FileNotFoundError:
        print("No se encontró el archivo de datos de transacciones.")
    except json.JSONDecodeError:
        print("Error al leer el archivo de datos de transacciones. El archivo puede estar corrupto o mal formateado.")
    except Exception as e:
        print(f"Error al generar el informe de ventas: {e}")

def generar_informe_compras(fecha_inicio_str, fecha_fin_str):
    if not (validar_fecha(fecha_inicio_str) and validar_fecha(fecha_fin_str)):
        print("Error: Las fechas deben estar en el formato 'YYYY-MM-DD' y ser válidas.")
        return

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
        
        if fecha_inicio > fecha_fin:
            print("Error: La fecha de inicio debe ser anterior a la fecha de fin.")
            return
        
        with open('data/compras.json', 'r') as file:
            data = json.load(file)
        
        compras = data.get('compras', [])
        total_costos = 0

        print(f"Informe de Compras desde {fecha_inicio_str} hasta {fecha_fin_str}:")
        for compra in compras:
            fecha_compra = datetime.strptime(compra['Fecha de la compra'], '%Y-%m-%d')
            if fecha_inicio <= fecha_compra <= fecha_fin:
                print(f"Fecha: {compra['Fecha de la compra']}")
                print(f"Proveedor: {compra['Nombre del proveedor']}")
                print(f"Dirección: {compra['Dirección del proveedor']}")
                print("Productos comprados:")
                for producto in compra['Productos']:
                    print(f"  Producto: {producto['Producto']}, Cantidad: {producto['Cantidad']}, Precio: {producto['Precio']}")
                    total_costos += float(producto['Precio']) * float(producto['Cantidad'])
                print()

        print(f"Total de costos en el período: {total_costos}")

    except FileNotFoundError:
        print("No se encontró el archivo de datos de compras.")
    except json.JSONDecodeError:
        print("Error al leer el archivo de datos de compras. El archivo puede estar corrupto o mal formateado.")
    except Exception as e:
        print(f"Error al generar el informe de compras: {e}")
