def suma(a,b):
    try:
        resultado=a+b
    except TypeError:
        print("Error: Tipo de dato no valido") 
    else:
        return resultado
            

def resta(a,b):
    try:
        resultado=a-b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return resultado

def producto(a,b): #es una multiplicacion
    try:
        resultado=a*b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return resultado

def division(a,b):
    try:
        resultado=a/b
    except TypeError:
        print("Error: Tipo de dato no valido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero ")     
    else:
        return resultado

#a=input("Ingresa un valor")
#b=input("Ingresa un nuevo valor")
a,b,c,d=(10,5,0,"hola")

print("{}+{}={}".format(a,b, suma(a,b)))
print("{}-{}={}".format(b,d, resta(b,d)))
print("{}*{}={}".format(b,b, producto(b,b)))
print("{}/{}={}".format(a,c, division(a,c)))
