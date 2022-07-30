# Escribe una función que calcule el área de un triángulo, 
# recibiendo la altura y la base como parámetros y otra función 
# que calcule el área de un círculo recibiendo el radio del mismo.

def areatriangulo(base, altura):
    area = base * altura/2
    print("El area del triangulo es igual a : " , area)


def areacirculo(radio):
    area = 3.14 * (radio ** 2)
    print("El area del triangulo es igual a : " , area)

base = 5
altura = 10
radio = 12
areatriangulo(base, altura)
areacirculo(radio)
