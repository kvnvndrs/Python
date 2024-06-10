'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def max_de_tres(a, b, c):
    if a > b:
        if a < c:
            return c
        elif a == c:
            return a
        else:
            return c
    elif a == b:
        if a < c:
            return c
        elif a == c:
            return a
        else:
            return a
    else:
        if b < c:
            return c
        elif b == c:
            return b
        else:
            return b

a = int(input("Dame un numero: "))
b = int(input("Dame otro numero: "))
c = int(input("Dame otro numero: "))
print(max_de_tres(a, b, c))