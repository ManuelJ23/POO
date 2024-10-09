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



class Computadora():
    # Constructor
    def __init__(self, marca, memoriaRam, procesador, tienePlacaGrafica, teclado, monitor):
        self._marca = marca
        self._memoriaRam = memoriaRam
        self._procesador = procesador
        self._tienePlacaGrafica = tienePlacaGrafica
        self._teclado = teclado
        self._monitor = monitor

    #Métodos de consulta

    def getMarca(self):
        return self._marca

    def getMemoriaRam(self):
        return self._memoriaRam

    def getProcesador(self):
        return self._procesador

    def getTienePlacaGrafica(self):
        return self._tienePlacaGrafica

    def getTeclado(self):
        return self._teclado

    def getMonitor(self):
        return self._monitor


    # Métodos de modificación

    def setMarca(self, nuevo):
        self._marca = nuevo

    def setMemoriaRam(self, nuevo):
        self._memoriaRam = nuevo

    def setProcesador(self, nuevo):
        self._procesador = nuevo

    def setTienePlacaGrafica(self, nuevo):
        self._tienePlacaGrafica = nuevo

    def setTeclado(self, nuevo):
        self._teclado = nuevo

    def setMonitor(self, nuevo):
        self._monitor = nuevo

class Computadora2():
    # Constructor
    def __init__(self, marca, memoriaRam, procesador, tienePlacaGrafica):
        self._marca = marca
        self._memoriaRam = memoriaRam
        self._procesador = procesador
        self._tienePlacaGrafica = tienePlacaGrafica
        self._teclado = None
        self._monitor = None

    #Métodos de consulta

    def getMarca(self):
        return self._marca

    def getMemoriaRam(self):
        return self._memoriaRam

    def getProcesador(self):
        return self._procesador

    def getTienePlacaGrafica(self):
        return self._tienePlacaGrafica

    def getTeclado(self):
        return self._teclado

    def getMonitor(self):
        return self._monitor


    # Métodos de modificación

    def setMarca(self, nuevo):
        self._marca = nuevo

    def setMemoriaRam(self, nuevo):
        self._memoriaRam = nuevo

    def setProcesador(self, nuevo):
        self._procesador = nuevo

    def setTienePlacaGrafica(self, nuevo):
        self._tienePlacaGrafica = nuevo


    #Métodos de operación

    def agregarTeclado(self, nuevoTeclado):
        self._teclado = nuevoTeclado

    def agregarMonitor(self, nuevoMonitor):
        self._monitor = nuevoMonitor