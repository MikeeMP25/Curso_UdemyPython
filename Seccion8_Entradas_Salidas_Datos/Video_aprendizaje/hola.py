#print("Hola, Bienvenido a tu primer script")
#la entreda de argumentos 
import sys

#esto se le conoce como un argumento del script 
#print(sys.argv)
#la lista de su argv

#print(sys.argv[1:])#esto es para mostrar lo que le enviamos en el script 

for argumento in sys.argv[1:]:
    print(argumento)#como ver me lo imprime uno a uno el contenido que entro en el script
    
