'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error. '''
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
try:
    result = num1 / num2
    print(int(result))
except ZeroDivisionError:
    print("ERROR. No puedes dividir entre cero")