x: int 
x=int(input("Inserte un numero: "))
if x == 97 or x == 101 or x == 105 or x == 111 or x == 117: 
    print("El numero es una vocal minuscula ")
else: 
    print("El numero no es es una vocal")




    
x=input("Ingrese una cadena de longitud 1: ")
a=ord (x)
if a % 2 == 0:
    print("el codigo ASCII de la primera letra de la cadenas es par")
else:
    print("el codigo ASCII de la primera letra de la cadenas es inpar")


    
s=int(input("Ingrese un solo caracter: "))
if  s>=0 and s<=9:
    print( " El caracter " + str(s) + " es un digito")
else:
    print( "el caracter " + str(s) + " no es un digito")


b=float(input("Ingrese un numero: "))
if b >0: 
    print("El numero es positivo")
elif b == 0:
    print("El numero es neutro para la suma")
else:
    print("El numero es negativo")



Cx=float(input("Ingrese la coordenada eje x del centro del círculo: "))
Cy=float(input("Ingrese la coordenada eje y del centro del círculo: "))
R = float(input("Ingrese el radio del círculo: "))
Rx=float (input("Ingrese la coodenada en x del punto R2: "))
Ry=float (input("Ingrese la coodenada en x del punto R2: "))

if ((Rx - Cx)**2 + (Ry - Cy)**2) <=R:
    print("El punto está dentro del círculo.")
else:
    print("El punto está fuera del círculo.")


a : float
b : float
c : float 
a = float(input("Inserte lado a del triangulo: "))
b = float(input("Inserte lado b del triangulo: "))
c = float(input("Inserte lado c del triangulo: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print( "Se puede construir el triangulo")
else:
    print( "No se puede construir el triangulo")

