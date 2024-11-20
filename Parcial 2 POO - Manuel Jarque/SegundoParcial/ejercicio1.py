# Manuel Jarque

class LimiteTemasError(Exception):
    def __init__(self, cantidadMaximaTemas):
        self._cantidadMaximaTemas = cantidadMaximaTemas

class NombreTemaLargoError(Exception):
    def __init__(self, nombre):
        self._nombre = nombre

class ListaDeReproduccion:
    # Completar la implementación necesaria
    def __init__(self, genero):
        self._genero = genero
        self._listaTemas = []
        self._cantidadMaximaTemas = 5


    def detallarTemas(self):
        print("Temas de la lista:")
        # Completar para imprimir información de cada tema
        for tema in self._listaTemas:
            print(f"-{tema}")


    def agregarTema(self, nombre, genero):
        # Implementar las excepciones indicadas en el enunciado

        if len(self._listaTemas) >= self._cantidadMaximaTemas:
            raise LimiteTemasError(self._cantidadMaximaTemas)

        if not isinstance(nombre, str):
            raise TypeError("El nombre de la canción debe ser de tipo str")

        if not isinstance(genero, str):
            raise TypeError("El género de la canción debe ser de tipo str")

        if nombre in self._listaTemas:
            raise ValueError(f"Error: el tema {nombre} ya se encuentra en la lista.")

        if genero != self._genero:
            raise ValueError(f"la lista solo puede tener temas de {self._genero}")

        if len(nombre) > 25:
            raise NombreTemaLargoError(nombre)

        self._listaTemas.append(nombre)