# Escribe una función que pueda decirte si 
# un año (número entero) es bisiesto o no.

from random import random


def esbisiesto(numero):
    if numero%4 == 0 and (numero % 100 != 0 or numero % 400 == 0):
        print("El año", numero , "Es bisiesto")
    else:
        print("El año", numero, "No es bisiesto")


esbisiesto(1996)
esbisiesto(1997)
esbisiesto(1998)
esbisiesto(1999)
esbisiesto(2000)
esbisiesto(2001)