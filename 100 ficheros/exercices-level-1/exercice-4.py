'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''
def CorV(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print("Es una vocal")
    else:
        print("Es consonante")

c = []
c = input("Dame un caracter: ")
CorV(c)