from Producto import Producto 

class Restaurant(Producto):
    def __init__(self, nombre, cantidad, precio, stock, tipo, package):
        super().__init__(package)
        self.package= package
    
    def __str__(self):
        return f"Package: {self.package}"

