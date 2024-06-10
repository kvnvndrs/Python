'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable,
  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
   índice de masa corporal calculado
 redondeado con dos decimales. '''

#round(a, b) para redondear, a es la variable a redondear y b es la cantidad de decimales

kg = float(input("Cual es su peso en kg? "))
alt = float(input("Cual es su altura en metros? "))
imc = kg/(alt*alt)
imc = round(imc, 2)
print("Su imc es de: ",imc)