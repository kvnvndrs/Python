'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''

while True:
    dia = input("Ingrese su dia de nacimiento: ")
    if len(dia)==2 or len(dia)==1:
        break
    else:
        print("La fecha que ingreso es invalida")

while True:
    mes = input("Ingrese su mes de nacimiento: ")
    if len(mes)==2 or len(mes)==1:
        break
    else:
        print("La fecha que ingreso es invalida")

while True:
    anio = input("Ingrese su año de nacimiento: ")
    if len(anio)==4:
        break
    else:
        print("La fecha que ingreso es invalida")

print("Su dia de nacimiento es el",dia,"del",mes,"del año",anio)