"""
En este segundo ejercicio, tenéis que crear una 
aplicación que obtendrá los elementos impares de 
una lista pasada por parámetro con filter y realizará 
una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def funcionverifica(x):
    if x % 2 != 0:
        return True
    return False

def funcionsuma(a, b):
    print(f'a={a}, b={b}')
    return a + b

resultado = filter(funcionverifica, lista)
listaimpares = list(resultado)
sumatotal = reduce(funcionsuma, listaimpares)
print(sumatotal)

