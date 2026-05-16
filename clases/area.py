class Area:
    def __init__ (self, area):
        self.__nombre_area = area
        self.__rubrica = []
        self.__observacion = ""
    
    def get_nombre_area(self):
        return self.__nombre_area
    
    def get_observacion(self):
        return self.__observacion
    def set_observacion(self, nueva_observacion):
        self.__observacion = nueva_observacion
        
    def agregar_rubrica(self, rubrica):
        self.__rubrica.append(rubrica)
    
    def mostrar_promedio(self):
        total = sum(self.__rubrica)
        promedio = total / len(self.__rubrica) if self.__rubrica else 0
        return promedio
    
    def obtener_desempeño(self):
        promedio = self.mostrar_promedio()
        if self.__rubrica:
            if promedio >= 4.5:
                return "Lo has logrado"
            elif promedio >= 3.0:
                return "Vas por buen camino"
            else:
                return "Falta mejorar"


        