numero = 12383974924
#a) Implementar una función que permita extraer la última cifra
# de un número entero positivo (es decir, la cifra de unidad).
# 1234 --> 4
ultimoDigito = numero % 10
print(ultimoDigito)
#b) Implementar una función que permita extraer todas las cifras excepto la última cifra de un número
# entero positivo (es decir, todas menos la cifra de unidad).
# 1234 --> 123
digitosRestantes = numero // 10
print(digitosRestantes)
#c) Implementar una función que devuelva la cantidad de cifras que contiene un número entero
# positivo.
# 1234 --> 4
"""numeroPalabra = str(numero)
print(len(numeroPalabra))"""
contarDigitos = 1
print(numero)
print('==============')
while numero > 9:
    #quitar un digito
    numero = numero // 10
    print(numero)
    #contar un digito
    contarDigitos = contarDigitos + 1
print(contarDigitos)