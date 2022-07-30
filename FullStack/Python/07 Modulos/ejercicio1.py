"""
En este ejercicio tendréis que crear un módulo que contenga 
las operaciones básicas de una calculadora: sumar, restar, 
multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis 
a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

import operaciones

def main():
    suma = operaciones.Operador.suma(1, 18)
    resta = operaciones.Operador.resta(75, 8)
    multiplicacion = operaciones.Operador.multiplicacion(3, 7)
    division = operaciones.Operador.division(750, 2)
    print("La suma es : ", suma)
    print("La resta es : ", resta)
    print("La multiplicacion es : ", multiplicacion)
    print("La division es : ", division)
    

if __name__ == '__main__':
    main()