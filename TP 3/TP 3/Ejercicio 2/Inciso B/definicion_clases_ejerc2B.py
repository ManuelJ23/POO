class AlbumMusical():
    def __init__(self, nombreAlbum):
        self._nombreAlbum = nombreAlbum
        self._temas = []


    def setNombreAlbum(self, nuevo):
        self._nombreAlbum = nuevo
        
    def getNombreAlbum(self):
        return self._nombreAlbum

    def getTemas(self):
        return self._temas

    def agregarTema(self, nombre, duracion, letra):
        unTema = Tema(nombre, duracion, letra)
        self._temas.append(unTema)


class Tema():
    def __init__(self, nombre, duracion, letra):
        self._nombre = nombre
        self._duracion = duracion
        self._letra = letra


    def setNombre(self, nuevo):
        self._nombre = nuevo
        
    def getNombre(self):
        return self._nombre

    def setDuracion(self, nuevo):
        self._duracion = nuevo

    def getDuracion(self):
        return self._duracion

    def setLetra(self, nuevo):
        self._letra = nuevo

    def getLetra(self):
        return self._letra


