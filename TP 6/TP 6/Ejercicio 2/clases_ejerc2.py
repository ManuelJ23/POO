class RangeError(Exception):
    def __init__(self, valor):
        self._valor = valor

class Pantalla():
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    def getAncho(self):
        return self._ancho
    
    def getAlto(self):
        return self._alto

    def dibujarPunto(self, x, y):
        # Los parámetros deben ser enteros
        if not isinstance(x, int):
            raise TypeError("El parámetro X debe ser de tipo entero")
        if not isinstance(y, int):
            raise TypeError("El parámetro Y debe ser de tipo entero")


        # x no puede ser negativo ni mayor al ancho de la pantalla
        if x < 0:
            raise RangeError(x)

        if x > self._ancho:
            raise RangeError(x)

        # y no puede ser negativo ni menor al alto de la pantalla
        if y < 0:
            raise RangeError(y)

        if y > self._alto:
            raise RangeError(y)

        return f"Punto dibujado en las coordenadas({x, y})"
