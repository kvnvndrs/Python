'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''

p = int(input("Cantidad de payasos ingresados: "))
m = int(input("Cantidad de muñecas ingresadas: "))
p = p*112
m = m*75
print("el peso de los payasos es de: ",p,"g y el de las muñecas es de: ",m,"g")