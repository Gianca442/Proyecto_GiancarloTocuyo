class Cliente:
    def __init__(self, nombre, cedula ,edad, vip):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.vip = vip
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}, Es VIP?: {self.vip}"
    

