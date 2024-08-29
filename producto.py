class Producto:
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)

    def nombre(self):
        return self.__nombre

    def precio(self):
        return self.__precio

    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, cantidad: int):
        self.__stock = max(0, cantidad)

    def __add__(self, other):
        if isinstance(other, Producto) and self.__nombre == other.__nombre:
            self.stock += other.stock
        return self

    def __sub__(self, cantidad: int):
        self.stock -= cantidad
        return self

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre == other.__nombre
        return False

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio:.2f} - Stock: {self.__stock}"
