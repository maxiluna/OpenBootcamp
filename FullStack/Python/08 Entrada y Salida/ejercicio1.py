"""
En este ejercicio, tendréis que crear un archivo py 
donde creéis un archivo txt, lo abráis y escribáis 
dentro del archivo. Para ello, tendréis que acceder 
dos veces al archivo creado
"""
def escribe(fichero, texto):
    f = open(fichero, 'w')
    for linea in texto:
        linea = linea
        f.write(linea)
    f.close()

def leer(fichero):
    f = open(fichero, 'r')
    for linea in f:
        print(linea) 
    f.close()

textoaguardar = [
    'Escribo algo\n',
    'sumo otro valor\n',
    'Finalizo la escritura\n'
]

escribe('mifichero.txt', textoaguardar)
leer('mifichero.txt')
