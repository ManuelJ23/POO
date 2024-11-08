class Numeros():
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def __iter__(self):
        return (num for num in self.lista_numeros if num > 0)