class NoSieteError(Exception):
    def __init__(self, texto):
        self._texto = f'{texto}'

    def getTexto(self):
        return self._texto

class Estandar():
    def __init__(self):
        self._valor = 0

    def setValor(self,nuevo):
        if isinstance(nuevo,int):
            if nuevo != 7:
                self._valor = nuevo
            else:
                raise NoSieteError('oops, no queremos los 7')
        else:
            raise TypeError()

    def getValor(self):
        return self._valor