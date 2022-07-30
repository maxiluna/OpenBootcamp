"""
En este segundo ejercicio, tendréis que crear un archivo py
y dentro crearéis una clase Vehículo, haréis un objeto de ella,
lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle

class Vehiculo():
    _marca = ""
    _precio = 0.0

    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def getMarca(self):
        return self.marca, self.precio

def escribe(fichero, objetos):
    with open(fichero, "wb") as f:
        pickle.dump(objetos, f)

def leer(fichero):
    with open(fichero, "rb") as f:
        datosdearchivo = pickle.load(f)
        print(datosdearchivo[0].marca)
        print(datosdearchivo[0].precio)
        print(datosdearchivo[1].marca)
        print(datosdearchivo[1].precio)
        print(datosdearchivo[2].marca)
        print(datosdearchivo[2].precio)
        print(datosdearchivo[3].marca)
        print(datosdearchivo[3].precio)

auto1 = Vehiculo("Chevrolet", 2000)
auto2 = Vehiculo("Peugeto", 3000)
auto3 = Vehiculo("Honda", 7000)
auto4 = Vehiculo("BMW", 10000)
objetos = [auto1, auto2, auto3, auto4]

escribe('mifichero.txt', objetos)
leer('mifichero.txt')
