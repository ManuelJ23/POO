class Sobre():
    #Constructor
    def __init__(self, ancho : float, alto : float):
        self._ancho = ancho
        self._alto = alto

    def __repr__(self):
        return f"Sobre({self._ancho}, {self._alto})"


    def setAncho(self, nuevoAncho):
        self._ancho = nuevoAncho

    def getAncho(self):
        return self._ancho

    def setAlto(self, nuevoAlto):
        self._alto = nuevoAlto

    def getAlto(self):
        return self._alto

    def __lt__(self, other):
        if isinstance(other, Sobre):
            if self._alto < other.getAlto() and self._ancho < other.getAncho():
                return True
            return False

    def __contains__(self, sobre):
        if isinstance(sobre, Sobre):
            return self._ancho >= sobre.getAncho() and self._alto >= sobre.getAlto()
        return False

    def __truediv__(self, other):
        if isinstance(other, int) and other > 0:
            div_alto = self._alto / other

            return [Sobre(div_alto, self._ancho) for _ in range(other)]
        else:
            raise ValueError("El divisor debe ser un número entero mayor que 0")
