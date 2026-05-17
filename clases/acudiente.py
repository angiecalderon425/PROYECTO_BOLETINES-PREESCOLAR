from clases.persona import Persona

class Acudiente(Persona):
    def __init__(self, nombre, edad, celular, parentesco):
        super().__init__(nombre, edad)
        self.__celular = celular
        self.parentesco = parentesco

    def get_celular(self):
        return self.__celular

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Celular: {self.get_celular()}, Parentesco: {self.parentesco}"
    