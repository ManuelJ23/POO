class A():
    def __init__(self,a1):
        self._a1 = a1

    def calcularCuadrado(self):
        return self._a1 ** 2

class B(A):
    def __init__(self,a1, b1):
        super().__init__(a1)
        self._b1 = b1

    def calcularCuadrado(self):
        return self._b1 ** 2

class C(B):
    def __init__(self, a1, b1):
        super().__init__(a1, b1)

    def sumar(self):
        return self._a1 + self._b1

