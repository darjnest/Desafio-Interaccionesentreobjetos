# Desafío - Interacciones entre objetos

Este desafío valida los conocimientos de abstracción, encapsulamiento, colaboración y composición en el paradigma de programación orientada a objetos en Python.

## Descripción

Participas en un proyecto de emprendimiento que consiste en una aplicación móvil para la compra y reparto de productos. El equipo ha decidido desarrollar el backend de la aplicación utilizando Python y el paradigma orientado a objetos. Para el primer prototipo, se solicita realizar una aplicación de consola en Python, donde los ingresos de valores se hagan mediante `input`.

### Consideraciones sobre las tiendas

- Existen 3 tipos de tienda: `Restaurante`, `Supermercado` y `Farmacia`.
- Todas las tiendas pueden ingresar un producto, listar los productos existentes, y realizar ventas.
- Cada tienda creada posee un nombre, un listado de productos y un costo de delivery.
- El nombre y el costo de delivery no pueden modificarse después de crear la tienda.
- Los productos tienen un nombre, un precio y un stock. El stock se asume en 0 si no se especifica.

### Comportamiento de cada tipo de tienda

1. **Restaurante**:

   - Los productos siempre tienen stock igual a 0.
   - El stock no se modifica al añadir nuevamente el mismo producto.

2. **Supermercado**:

   - Al listar los productos, se muestra el mensaje “Pocos productos disponibles” si el stock es inferior a 10.

3. **Farmacia**:
   - Se añade el mensaje “Envío gratis al solicitar este producto” junto al precio de los productos con un valor superior a $15.000.
   - No se puede solicitar una cantidad superior a 3 unidades de un producto en cada venta.

## Requerimientos

1. **Definir la clase `Producto`** en `producto.py`:

   - Implementar el encapsulamiento.
   - Definir un constructor que permita instanciar productos con nombre, precio y stock.
   - Los atributos de la clase deben ser privados y accesibles solo mediante métodos o propiedades.

2. **Definir la o las clases necesarias para instanciar tiendas** en `tienda.py`:

   - Utilizar abstracción y encapsulamiento.
   - Implementar un constructor para cada tipo de tienda.
   - Crear métodos para ingresar productos, listar productos y realizar ventas.
   - Usar composición para manejar los productos dentro de cada tienda.

3. **Implementar la lógica principal** en `programa.py`:
   - Permitir la creación de una tienda e ingreso de productos mediante `input`.
   - Ofrecer opciones para listar productos, realizar ventas o salir del programa.

## Estructura de Archivos

.
├── producto.py # Definición de la clase Producto
├── tienda.py # Definición de las clases de tiendas
└── programa.py # Lógica principal del programa

## Uso

Ejecutar el archivo programa.py para iniciar la aplicación. Sigue las instrucciones en la consola para crear tiendas, ingresar productos, listar productos y realizar ventas.

## Ejecucion

$ python programa.py
