""" 
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    Color
    Ruedas
    Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
    Velocidad
    Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""

class Vehiculo:
    color = ""
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

audi = Coche()
audi.cilindrada = 100
audi.color = "Blanco"
audi.puertas = 5
audi.velocidad = 180
audi.ruedas = 5

print(audi.cilindrada)
print(audi.color)
print(audi.puertas)
print(audi.velocidad)
print(audi.ruedas)