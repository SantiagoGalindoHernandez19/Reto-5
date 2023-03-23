# Reto-5

Dado un número entero, determine si ese número corresponde al código ASCII de una minúscula vocal.



n: int

x=int(input("Inserte un numero"))

if x == 97 or x == 101 or n == 105 or n == 111 or n == 117: 

    print("El numero es una vocal minuscula ")
else: 
    print("El numero no es es una vocal")




Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.

x=input("Ingrese una cadena de longitud 1: ")

a=ord (x)

if a % 2 == 0:

    print("el codigo ASCII de la primera letra de la cadenas es par")
    
else:
    print("el codigo ASCII de la primera letra de la cadenas es inpar")
    
    
