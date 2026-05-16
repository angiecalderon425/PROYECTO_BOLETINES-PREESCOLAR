from clases.persona import Persona

class Profesor (Persona):
    def __init__ (self, nombre, edad, genero, curso):
        super().__init__(nombre, edad)
        self.curso = curso
        self.genero = genero

    def mostrar_datos(self):
        return f" Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Curso: {self.curso}"
    