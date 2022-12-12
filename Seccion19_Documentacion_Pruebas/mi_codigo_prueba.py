def doblar(lista):
    """
    Dobla el valor de los elementos de una lista 

    >>> l=[1, 2, 3, 4, 5]  #Es una linea de codigo
    >>> doblar(l) #dos lineas de comandos
    [2, 4, 6, 8, 10] #resultado 
    
    >>> l=[]
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [n*2 for n in lista]

    #vamos hacer varias lineas de test en donde ahi codigo  

if __name__ =="__main__":
    import doctest
    doctest.testmod()