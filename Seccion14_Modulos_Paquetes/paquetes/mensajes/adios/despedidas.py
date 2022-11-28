def despedir():
   print("adios , me despido desde despedidas. despddir()")

class Despedida:
    
    def __init__(self):
        
        print("Adios, me despido desde Despedida.__init__() ")


#con esta comparacion podemos evitar que se ejecute esta parte del codigo al momento de importar el modulo... 
if __name__ == '__main__':
     despedir()