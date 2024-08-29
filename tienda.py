from math import prod
from producto import Producto


class Tienda:
    def __init__(self, nombre: str, costo_delivery: float):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def nombre(self):
        return self.__nombre

    def costo_delivery(self):
        return self.__costo_delivery

    def agregar_producto(self, producto: Producto):
        for p in self.__productos:
            if p == producto:
                p += producto
                return
        self.__productos.append(producto)

    def listar_productos(self):
        return "\n".join(str(p) for p in self.__productos)

    def vender_producto(self, nombre: str, cantidad: int):
        for p in self.__productos:
            if p.nombre == nombre:
                p - cantidad
                return f"Venta realizada: {nombre} - Cantidad: {cantidad}"
        return "Producto no encontrado o stock insuficiente."


class Restaurante(Tienda):
    def agregar_producto(self, producto: Producto):
        producto.stock = 0
        super().agregar_producto(producto)

    def listar_productos(self):
        return "\n".join(
            f"{p.nombre} - ${p.precio:.2f}" for p in self._Tienda__productos
        )


class Supermercado(Tienda):
    def listar_productos(self):
        productos_listados = []
        for p in self._Tienda__productos:
            mensaje = f"{p.nombre} - ${p.precio:.2f} - Stock: {p.stock}"
            if p.stock < 10:
                mensaje += " (Pocos productos disponibles)"
            productos_listados.append(mensaje)
        return "\n".join(productos_listados)


class Farmacia(Tienda):
    def listar_productos(self):
        productos_listados = []
        for p in self._Tienda__productos:
            mensaje = f"{p.nombre} - ${p.precio:.2f}"
            if p.precio > 15000:
                mensaje += " (Envío gratis al solicitar este producto)"
            productos_listados.append(mensaje)
        return "\n".join(productos_listados)

    def vender_producto(self, nombre: str, cantidad: int):
        if cantidad > 3:
            return "No se puede vender más de 3 unidades por producto."
        return super().vender_producto(nombre, cantidad)
