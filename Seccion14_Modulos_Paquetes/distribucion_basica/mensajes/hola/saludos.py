def saludar():
   print("hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una prueba de la nueva version")
    
class Saludo:
    
    def __init__(self):
        
        print("Hola, te saludo desde Saludo.__init__() ")

#mensaje="Bievenido a codigo python desarrollador junir"
#print(__name__)
#con esta comparacion podemos evitar que se ejecute esta parte del codigo al momento de importar el modulo... 
if __name__ == '__main__':
     saludar()