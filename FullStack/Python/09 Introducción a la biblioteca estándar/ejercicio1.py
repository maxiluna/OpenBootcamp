"""
Crea un script que le pida al usuario una lista de países 
(separados por comas). Éstos se deben almacenar en una lista. 
No debería haber países repetidos (haz uso de set). Finalmente,
muestra por consola la lista de países ordenados alfabéticamente 
y separados por comas.
"""
paises = set()
#Funcion recursiva con limite de 5
def agregapais():
    paises.add(input("Introduzca un pais: "))
    if (len(paises)<5):
        agregapais()

agregapais()
print(sorted(paises), sep=',')