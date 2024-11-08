from clasesTP5 import *

objeto1 = Dos(5)
print(objeto1.getValor())

try:
    objeto1.incrementarValor(4)
except Exception as ex:
    if isinstance(ex,TypeError):
        print('che el valor se te fue por encima de 10')


print(objeto1.getValor())

try:
    objeto1.incrementarValor(4)
except Exception as ex:
    if isinstance(ex,TypeError):
        print('che el valor se te fue por encima de 10')
#finally:
#    objeto1.reducirValor(4)
# es opcional...
print(objeto1.getValor()) # esperaria 13

try:
    objeto1.reducirValor(50)
except Exception as ex:
    if isinstance(ex,LogicaError):
        print(ex.getTexto())
    elif isinstance(ex, TypeError):
        print('oop un error de tipo')

print('=========================================')

try:
    miPrecio1 = Precio("1000")
except Exception as ex:
    print(ex)


















