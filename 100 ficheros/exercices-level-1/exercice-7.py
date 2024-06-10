'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def inversa(cadena):
    return cadena[::-1]

def palindromo(cadena):
    inv = inversa(cadena)
    return inv == cadena

print(palindromo(input("Dame una cadena: ")))