'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''

n = int(input("Dame un numero: "))
m = int(input("Dame otro numero: "))
c = n / m
r = n % m
print("la n es ", n ,", m es ", m ,", su cociente es ", int(c) ,", y el residuo es ", r)