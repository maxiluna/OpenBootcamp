"""
En este segundo ejercicio, tendréis que crear un programa que tenga
 una clase llamada Alumno que tenga como atributos su nombre y su nota. 
 Deberéis de definir los métodos para inicializar sus atributos, 
 imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    _nombre = ""
    _nota = ""

    def __init__(self):
        self.nombre = ""
        self.nota = 0
    
    def esAprobado(self):
        if (self.nota > 4):
            print("Alumno", self.nombre, "- Nota:", self.nota, "- Aprobado")
        else:
            print("Alumno", self.nombre, "- Nota:", self.nota, "- NO Aprobado")



alumno1 = Alumno()
alumno1.nombre = "Mateo"
alumno1.nota = 8
alumno1.esAprobado()

alumno2 = Alumno()
alumno2.nombre = "Alberto"
alumno2.nota = 4
alumno2.esAprobado()