from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto


def main():
    print("Bienvenido a la tiendita")
    tipo_tienda = (
        input("Seleccione el tipo de tienda (restaurante/supermercado/farmacia): ")
        .strip()
        .lower()
    )
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    if tipo_tienda == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    while True:
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(
                input("Ingrese el stock del producto (0 si no se indica): ")
            )
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.agregar_producto(producto)
        elif opcion == "2":
            print("\nProductos disponibles:")
            print(tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad_producto = int(input("Ingrese la cantidad a vender: "))
            print(tienda.vender_producto(nombre_producto, cantidad_producto))
        elif opcion == "4":
            print("Gracias por usar la aplicación.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
