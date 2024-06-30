class Boleto:
    def __init__(self, id, clase, precio, partido, asiento ):
        self.id = id
        self.clase = clase
        self.precio = precio
        self.partido = partido
        self.asiento = asiento
    def __str__(self):
        return f"Cedula: {self.id}, Clase: {self.clase}, Precio;{self.precio}, Partido: {self. partido}, Asiento: {self.asiento}"