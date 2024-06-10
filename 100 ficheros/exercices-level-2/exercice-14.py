'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''

hr = int(input("Cuantas horas trabajó? "))
coste = float(input("Cual es el coste por hora de trabajo? "))
paga = hr*coste
print("La paga que le corresponde es de: ",paga)