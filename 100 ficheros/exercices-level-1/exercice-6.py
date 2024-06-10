'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''

def inversa(cadena):
    inv = ""
    x = len(cadena) -1
    while x >= 0:
        inv += cadena[x]
        x-=1

    return inv

print(inversa(input("Dame una cadena: ")))