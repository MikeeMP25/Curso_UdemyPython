def palindromo(palabra):
  #  """
   # La funcion suma(a,b) recibe dos parametros a y b 
    #Devuelve la suma de ambos
    #>>> suma(5,10)
    #15
    #>>> suma(0,0)
    #1
    #>>> suma(-5,7)
    #2
    #"""
    #return a+b

    """La funcion palidromo(palabra) recibe una palabra.
    Si la palabra es un palindromo devuelve True, sino false
    Un palindromo es una palabra o frase que se lee igual tanto de izquierda a derecha
    como de derecha a izquierda

    >>> palindromo("radar")
    True
    >>> palindromo("somos")
    True
    >>> palindromo("holah")
    False
    >>> palindromo("Ana")
    True

    """
    if palabra.lower() == palabra[::-1].lower():
        return True
    else:
        return False

if __name__=="__main__":
    import doctest
    doctest.testmod()
