'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

cant = float(input("Que cantidad desea invertir? "))
anual = float(input("Cuanto es el interes anual? "))
anios = int(input("Por cuantos años invertira? "))
anual = cant*anual*anios*0.01
cap = cant + anual
print(cap)