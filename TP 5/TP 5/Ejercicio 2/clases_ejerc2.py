from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def incrementarValor(self, cantidad):
        pass


    @abstractmethod
    def reducirValor(self, cantidad):
        pass


class B(A):
    def __init__(self, valor):
        self._valor = valor

    def __str__(self):
        return f"Valor: {self._valor}"

    def incrementarValor(self, cantidad):
        self._valor += cantidad

    def reducirValor(self, cantidad):
        self._valor -= cantidad
