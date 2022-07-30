"""
En este segundo ejercicios tendréis que crear un script que nos 
diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. 
Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajar
"""

import time
from time import strftime
from time import gmtime

def main():
    horaactual = gmtime()
    horadesalida = gmtime(673200)

    if (horaactual.tm_hour < horadesalida.tm_hour):
        horas = horadesalida.tm_hour - horaactual.tm_hour
        minutos = 60 - horaactual.tm_min
        print("Quedan para trabajar", horas, "horas y ", minutos, "minutos")
    else:
        print("Ya es la hora de irse")
        
if __name__ == '__main__':
    main()

