'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde 
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el
 número de teléfono sin el prefijo y la extensión.'''
num = input("Número de teléfono: ")
num_sin_prefijo = num[4:]
num_final = num_sin_prefijo[:-3]
print(num_final)