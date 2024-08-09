# Trabajo_Python_CorzoAyelmer

## 📖 Descripción

Este proyecto es una aplicación en Python para gestionar ventas y compras en una panadería. Permite registrar transacciones de venta, registrar compras de proveedores, y generar informes detallados sobre ventas y stock.

## 🚀 Características

- **Ventas**:
  - Registrar transacciones de venta con información detallada.
  - Agregar múltiples productos a una transacción.
  
- **Compras**:
  - Registrar compras realizadas a proveedores.
  - Soporte para múltiples productos por compra.

- **Informes**:
  - Generar informes de ventas en un período específico.
  - Generar informes de stock para gestionar inventarios.

## 🛠️ Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/ayelmercorzo/Trabajo_Python_CorzoAyelmer.git
   cd Trabajo_Python_CorzoAyelmer
2. **Configura el entorno**:

Asegúrate de tener Python 3.8 o superior instalado. Puedes usar un entorno virtual para manejar las dependencias.
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows usa `venv\Scripts\activate`

## 🏗️ Uso

1. **Ejecuta la aplicación**:

    ```bash
    python main.py

## Menú Principal:

1. Venta: Registra una nueva venta.
2. Compra: Registra una nueva compra.
3. Generar Informes: Genera informes de ventas y stock.

## Registro de Ventas:

Selecciona la opción para registrar una venta.
Introduce la fecha, información del cliente, empleado, y detalles de los productos vendidos.


Ingrese la fecha de la transacción: 2024-08-08
Ingrese el nombre del cliente: Juan Pérez
Ingrese la dirección del cliente: Calle Falsa 123
Ingrese nombre del empleado: Ana Gómez
Ingrese su cargo: Cajera
Ingrese el tipo de producto (panaderia, pasteleria, bebidas, promociones): panaderia
Producto: Pan de Bono
Cantidad: 10
Precio: 700
Puedes agregar múltiples productos.

## Registro de Compras:

Selecciona la opción para registrar una compra.
Introduce la fecha, información del proveedor, y detalles de los productos comprados.


- Ingrese la fecha de la Compra: 2024-08-08
- Ingrese el nombre del Proveedor: Postobon
- Ingrese el contacto del Proveedor: 3134277875
- Ingrese nombre del Producto comprado: Pan Bimbo
- Ingrese la cantidad de Productos: 22
- Ingrese el precio del Producto: 50000

## Generación de Informes:

Selecciona la opción para generar un informe.
Introduce el rango de fechas para el informe de ventas.


Ingrese la fecha de inicio (YYYY-MM-DD): 2024-08-01
Ingrese la fecha de fin (YYYY-MM-DD): 2024-08-31
Genera un informe de stock para ver el inventario actual.

# 📊 Informes
## Informe de Ventas

Listado de todas las ventas realizadas en un período de tiempo específico.
Incluye detalles de los productos vendidos y el total de ingresos.

## Informe de Stock:

Listado de todos los productos con su cantidad en stock.
Permite gestionar el inventario de manera proactiva.
🧩 Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación.
- `ui/menus.py`: Funciones para mostrar menús y manejar la interacción del usuario.
- `modules/aggCompra.py`: Funciones para agregar y manejar datos de compras.
- `modules/aggTransaccion.py`: Funciones para agregar y manejar datos de ventas.
- `modules/corefiles.py`: Funciones para iniciar y gestionar bases de datos.
- `modules/funcionGlobal.py`: Funciones globales para operaciones comunes.
- `modules/movesJson.py`: Funciones para manejar archivos JSON.
