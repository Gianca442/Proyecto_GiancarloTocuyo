from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, cantidad, precio, stock, tipo, alcoholica, no_alcoholica ):
        super().__init__(nombre, cantidad, precio, stock, tipo)
        self.alcoholica = alcoholica
        self.no_alcoholica = no_alcoholica

    def __str__(self):
        return f"Alcoholica: {self.alcoholica}, No Alcoholica: {self.no_alcoholica}"