'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''

def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False

lista1 = ['1','2','3','4','5']
lista2 = ['6','7','8','9','1']
print(superposicion(lista1,lista2))