'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def longitud(cadena):
    x = 0
    for i in cadena:
        x+=1
    return x

cadena = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(longitud(cadena))