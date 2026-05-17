class Boletin:
    def __init__ (self, estudiante, periodo):
        self.estudiante = estudiante
        self.periodo = periodo
        self.areas = []

    def agregar_area(self, area):
        self.areas.append(area)
    
    
    def mostrar_boletin(self):
        print("\n" + "="*70)
        print("                    BOLETÍN INFORMATIVO")
        print("="*70)

        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Periodo: {self.periodo}        Año: 2026        Grado: {self.estudiante.grado}")

        print("-"*70)
        print(f"{'DIMENSIÓN':<20}{'OBSERVACIÓN':<60}{'LOGRO':<20}")
        print("-"*70)

        for area in self.areas:
            print(f"{area.get_nombre_area():<20}"
                  f"{area.get_observacion()[:55]:<60}"
                  f"{area.obtener_desempeño():<20}")

        print("="*70)
        print("                FIRMA DEL DOCENTE:_________________")
        print("="*70)