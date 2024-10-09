class Libro():

    #Constructor
    def __init__(self, autor, titulo, genero, cantidadPaginas):
        self._autor = autor
        self._titulo = titulo
        self._genero = genero
        self._cantidadPaginas = cantidadPaginas

    #Comandos de consulta
    def getAutor(self):
        return self._autor

    def getTitulo(self):
        return self._titulo

    def getGenero(self):
        return self._genero

    def getCantidadPaginas(self):
        return self._cantidadPaginas

    #Comandos de modificación
    def setAutor(self, nuevoAutor):
        self._autor = nuevoAutor

    def setTitulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo

    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def setCantidadPaginas(self, nuevaCantidad):
        self._cantidadPaginas = nuevaCantidad

    #Comandos especiales
    def equals(self, obj2):
        if isinstance(obj2, Libro):
            if (self._autor == obj2.getAutor()
            and self._titulo == obj2.getTitulo()
            and self._genero == obj2.getGenero()
            and self._cantidadPaginas == obj2.getCantidadPaginas()):
                return True #Coinciden todos los valores
            else:
                return False #Algún valor no coincide
        else:
            return False #el obj2 no es de la misma clase, no puede ser igual

    def copy(self, obj2):
        if isinstance(obj2, Libro):
            self._autor = obj2.getAutor()
            self._titulo = obj2.getTitulo()
            self._genero = obj2.getGenero()
            self._cantidadPaginas = obj2.getCantidadPaginas()
        return obj2

    def clone(self):
        nuevoLibro = Libro(self._autor, self._titulo, self._genero, self._cantidadPaginas)
        return nuevoLibro

