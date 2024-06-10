import math

def chicharronera(a, b, c):
    discriminante = b*b - 4*a*c
    if discriminante < 0:
        return "La ecuación no tiene soluciones reales"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
print(chicharronera(a, b, c))