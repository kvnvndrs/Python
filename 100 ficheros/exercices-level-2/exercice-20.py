'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''

pan = int(input("Cuantos panes que no son del dia vendio? "))
pan = pan * 3.49
pan = round(pan,2)
pant = pan * 0.40
print("Coste por panes que no son del dia: ",pant,", su precio habitual seria de: ",pan)