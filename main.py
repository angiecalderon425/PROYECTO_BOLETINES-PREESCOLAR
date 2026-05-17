from clases.estudiante import Estudiante
from clases.area import Area
from clases.boletin import Boletin
from clases.acudiente import Acudiente
from clases.excepciones import NotaInvalidaError

estudiante1 = Estudiante("Emmanuel Alvarez Jerez", 5, "Masculino", "Transición-5")

area1 = Area("Cognitiva")
notas = [4,4,5,4,5]

for nota in notas:
    area1.agregar_rubrica(nota)

area2 = Area("Comunicativa")
notas = [5,4,4,5,4]

for nota in notas:
    area2.agregar_rubrica(nota)

area3 = Area("Socio-afectiva")
notas = [4,3,4,4,5]

for nota in notas:
    area3.agregar_rubrica(nota)

area4 = Area("Motora")
notas = [4,4,3,5,3]

for nota in notas:
    area4.agregar_rubrica(nota)


boletin1 = Boletin(estudiante1, "Primer Periodo")
boletin1.agregar_area(area1)
boletin1.agregar_area(area2)
boletin1.agregar_area(area3)
boletin1.agregar_area(area4)

boletin1.mostrar_boletin()

print("""
====================================
 SISTEMA DE BOLETINES PREESCOLAR
====================================

1. Registrar estudiante
2. Registrar acudiente
3. Crear boletín
4. Ver boletín
5. Salir
""")

estudiantes = []
acudientes = []
boletines = []
while True:
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        genero = input("Ingrese el género del estudiante: ")
        grado = input("Ingrese el grado del estudiante: ")
        nuevo_estudiante = Estudiante(nombre, edad, genero, grado)
        estudiantes.append(nuevo_estudiante)
        print("Estudiante registrado exitosamente")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del acudiente: ")
        edad = int(input("Ingrese la edad del acudiente: "))
        celular = input("Ingrese el número de celular del acudiente: ")
        parentesco = input("Ingrese el parentesco con el estudiante: ")
        nuevo_acudiente = Acudiente(nombre, edad, celular, parentesco)
        acudientes.append(nuevo_acudiente)
        print("Acudiente registrado exitosamente")

    elif opcion == "3":
       if estudiantes:
        print("Estudiantes registrados:")

        for estudiante in estudiantes:
            print(f"- {estudiante.nombre}, Edad: {estudiante.edad}, Grado: {estudiante.grado}")

        nombre_busqueda = input("Ingrese el nombre del estudiante para crear boletín: ")

        for estudiante in estudiantes:
            if estudiante.nombre == nombre_busqueda:
                periodo = input("Ingrese el periodo del boletín: ")

                nuevo_boletin = Boletin(estudiante, periodo)
        
                for i in range(4):
                  nombre_area = input("Ingrese el nombre del área: ")
                  nueva_area = Area(nombre_area)

                  for j in range(5):
                    while True:
                      try:
                         nota = float(input(f"Ingrese la nota {j+1} para el área {nombre_area}: "))
                         
                         if nota < 0 or nota > 5:
                            raise NotaInvalidaError()
                         
                         nueva_area.agregar_rubrica(nota)
                         break
                      except NotaInvalidaError as e:
                          print(e)

                  observacion = input(f"Ingrese una observación para el área {nombre_area}: ")
                  nueva_area.set_observacion(observacion)
                  nuevo_boletin.agregar_area(nueva_area)
                  
                
                boletines.append(nuevo_boletin)
                print("Boletín creado correctamente")

                nuevo_boletin.mostrar_boletin()
                break
       else:
          print("No hay estudiantes registrados.")

    elif opcion == "4":
      if boletines:
                print("Boletines registrados:")

                for boletin in boletines:
                    print(f"\nEstudiante: {boletin.estudiante.nombre}, Periodo: {boletin.periodo}")

                    for area in boletin.areas:
                        print(f"\nÁrea: {area.get_nombre_area()}, Promedio: {area.mostrar_promedio()}, Desempeño: {area.obtener_desempeño()}, Observación: {area.get_observacion()}")

      else:
            print("No hay boletines registrados.")


    elif opcion == "5":
        print("Salir")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
    





