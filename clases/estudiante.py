from clases.persona import Persona

class Estudiante (Persona):
    def __init__ (self, nombre, edad, genero, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        self.genero = genero

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Grado: {self.grado}"
    
        