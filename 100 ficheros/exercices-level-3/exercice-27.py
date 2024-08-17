'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''

email = input("Ingrese su correo electronico: ")
indice = email.find('@')
subEmail = email[0:indice]
print(subEmail+"@ceu.es")