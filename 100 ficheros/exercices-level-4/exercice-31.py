'''Escribir un programa que pregunte el nombre de un producto, 
su precio y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades
 con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

nom = input("Nombre del producto: ")
price = float(input("Precio del producto: "))
unit = int(input("Cantidad de unidades que desea registrar: "))
total = price * unit
prices = f"{price:8.2f}"
unit_str = f"{unit:3d}"
total_str = f"{total:10.2f}"
print(f"Nombre del producto: {nom}, precio unitario: {prices}, número de unidades: {unit_str}, coste total: {total_str}")