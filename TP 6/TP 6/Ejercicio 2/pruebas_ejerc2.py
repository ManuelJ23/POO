from clases_ejerc2 import *

miPantalla = Pantalla(30, 20)

# Prueba de tipo incorrecto
try:
    miPantalla.dibujarPunto("10", 19)
except TypeError as ex:
    print(ex)


# Prueba: x fuera de rango (negativo)
try:
    miPantalla.dibujarPunto(-1, 19)
except RangeError as ex:
    x = ex.args[0]
    print(f"el valor de x ({x}) no puede ser negativo.")


# Prueba: x fuera de rango (mayor que el ancho)
try:
    miPantalla.dibujarPunto(31, 10)
except RangeError as ex:
    x = ex.args[0]
    print(f"El valor de X ({x}) excede el ancho permitido ({miPantalla.getAncho()}).")


# Prueba: y fuera de rango (negativo)
try:
    miPantalla.dibujarPunto(23, -5)
except RangeError as ex:
    y = ex.args[0]
    print(f"El valor de Y ({y}) no puede ser negativo.")


# Prueba: y fuera de rango (mayor que el alto)
try:
    miPantalla.dibujarPunto(23, 34)
except RangeError as ex:
    y = ex.args[0]
    print(f"El valor de Y ({y}) excede el alto permitido ({miPantalla.getAlto()}).")