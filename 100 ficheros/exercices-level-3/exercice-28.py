'''Escribir un programa que pregunte por consola el precio de un
 producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''
precio = input("Precio del producto: ")
punto = precio.find('.')
print("El coste de su producto es de",precio[0:punto],"euros con",precio[punto+1:punto+3],"centimos")