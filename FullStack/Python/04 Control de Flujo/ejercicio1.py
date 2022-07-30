## Escribe un programa que pregunte al usuario su edad 
## y muestre por pantalla si es mayor de edad o no.

edad = input("Cual es su edad? : ")
if int(edad) >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")