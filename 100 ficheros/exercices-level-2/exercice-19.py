'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
 de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
 Redondear cada cantidad a dos decimales.'''

cant = float(input("Cantidad a ahorrar: "))
interes = cant*0.04
j = 1
for i in range(12):
    cant = interes + cant
    print("Mes numero ",j,":",cant)
    j+=1
print("Su ahorro al finalizar el año es de: ",cant)