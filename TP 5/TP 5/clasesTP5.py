class A():
    def __init__(self,a):
        self._a1 = a

    def getA(self):
        return self._a1

    def calcularCuadrado(self):
        return self._a1*self._a1

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self._b1 = b


    def getB(self):
        return self._b1

    def calcularCuadrado(self):
        return self._b1*self._b1

class C(B):
    def __init__(self,a,b):
        super().__init__(a,b)

    def sumar(self):
        #return self.getA() + self.getB()
        #return self._a1 + self._b1
        return super()._a1 + super()._b1

from abc import ABC, abstractmethod

class Uno(ABC):
    def __init__(self,valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    @abstractmethod
    def incrementarValor(self,cantidad):
        pass

    @abstractmethod
    def reducirValor(self, cantidad):
        pass

class CarlosError(Exception):
    def __init__(self,texto):
        self._texto = texto

class LogicaError(Exception):
    def __init__(self,texto):
        self._texto =f'mi mensaje es: {texto}'

    def getTexto(self):
        return self._texto

class Dos(Uno):
    def __init__(self, valor):
        super().__init__(valor)

    def incrementarValor(self, cantidad):
        # si valor es mayor que 10 entonces lanzo un error
        self._valor = self._valor + cantidad
        if self._valor > 10:
            raise TypeError()

    def reducirValor(self, cantidad):
        self._valor = self._valor - cantidad
        # si el valor es negativo lanzo un CarlosError
        if self._valor <0:
            raise LogicaError('mi error personalizado de jacqueline')

class Precio():
    def __init__(self,*args): # args va a ser una tupla
        self._precioLista = args[0]
        if len(args)==1:
            if isinstance(args[0],int):
                self._precioLista = args[0]
                self._descuento = 0
                self._recargo = 0
            else:
                raise TypeError('explicacion super cool..1')
        elif isinstance(args[1], int):
            self._precioLista = args[0]
            self._descuento = args[1]
            self._recargo = 0
        elif isinstance(args[1], tuple):
            self._precioLista = args[0]
            self._descuento = args[1][0]
            self._recargo = args[1][1]
        else:
            raise TypeError('explicacion super cool..2')

