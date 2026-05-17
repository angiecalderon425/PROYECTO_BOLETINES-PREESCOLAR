from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__( self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def mostrar_datos(self):
        pass