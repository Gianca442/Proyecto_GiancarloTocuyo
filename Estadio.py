class Estadio:
    def __init__(self,nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def __str__(self):
        return f"Estadio {self.nombre} - Ubicación: {self.ubicacion}"
    