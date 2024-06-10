'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''

def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def multip(lista):
    mult = 1
    for i in lista:
        mult *= i
    return mult

lista = [1,2,3,4]
print(sum(lista))
print(multip(lista))