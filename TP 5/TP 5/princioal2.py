from clasesDeErrores import *

instanciaEstandar = Estandar()

try:
    instanciaEstandar.setValor(7)
except Exception as ex:
    if isinstance(ex, TypeError):
        print('el valor ingresado debe ser de tipo entero')
    elif isinstance(ex,NoSieteError):
        print(ex.getTexto())

try:
    instanciaEstandar.setValor(5.1)
except Exception as ex:
    if isinstance(ex, TypeError):
        print('el valor ingresado debe ser de tipo entero')
    elif isinstance(ex,NoSieteError):
        print(ex.getTexto())

try:
    instanciaEstandar.setValor(3)
except Exception as ex:
    if isinstance(ex, TypeError):
        print('el valor ingresado debe ser de tipo entero')
    elif isinstance(ex,NoSieteError):
        print(ex.getTexto())

print(instanciaEstandar.getValor())