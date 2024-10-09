class Monitor():

    #Constructor

    def __init__(self, marca, tamanio, tipoPantalla, tipoConexion):
        self._marca = marca
        self._tamanio = tamanio
        self._tipoPantalla = tipoPantalla
        self._tipoConexion = tipoConexion


    #Métodos de consulta

    def getMarca(self):
        return self._marca

    def getTamanio(self):
        return self._tamanio

    def getTipoPantalla(self):
        return self._tipoPantalla

    def getTipoConexion(self):
        return self._tipoConexion

    #Comandos de Modificación

    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def setTamanio(self, nuevoTamanio):
        self._tamanio = nuevoTamanio

    def setTipoPantalla(self, nuevoTipoPantalla):
        self._tipoPantalla = nuevoTipoPantalla

    def setTipoConexion(self, nuevoTipoConexion):
        self._tipoConexion = nuevoTipoConexion



class Teclado():

    #Constructor
    def __init__(self, marca, lenguaje, incluyeNumPad, incluyeRetroIlum):
        self._marca = marca
        self._lenguaje = lenguaje
        self._incluyeNumPad = incluyeNumPad
        self._incluyeRetroIlum = incluyeRetroIlum


    #Comandos de Consulta
    def getMarca(self):
        return self._marca

    def getLenguaje(self):
        return self._lenguaje

    def getIncluyeNumPad(self):
        return self._incluyeNumPad

    def getIncluyeRetroIlum(self):
        return self._incluyeRetroIlum

    #Comandos de Modificación

    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def setLenguaje(self, nuevoLenguaje):
        self._lenguaje = nuevoLenguaje

    def setIncluyeNumPad(self, estadoNumPad):
        self._incluyeNumPad = estadoNumPad

    def setIncluyeRetroIlum(self, estadoRetroIlum):
        self._incluyeRetroIlum = estadoRetroIlum



