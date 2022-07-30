# Escribe una función que pueda decirte si un número 
# (número entero) es primo o no.

def esnumeroprimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if (esnumeroprimo(9) == True):
    print("Es numero primo")
else:
    print("No es numero primo")
