class Encomienda():

    #Constructor
    def __init__(self, remitente, destinatario, peso, dimensiones, costo):
        self._remitente = remitente
        self._destinatario = destinatario
        self._peso = peso
        self._dimensiones = dimensiones
        self._costo = costo
        self._estado = "Pendiente de despacho"
        self._estadosEnvio = ["Pendiente de despacho", "Despachado", "En viaje",
                   "Visita a domicilio", "Recibido", "Rechazado"]


    #Comandos de consulta
    def getRemitente(self):
        return self._remitente

    def getDestinatario(self):
        return self._destinatario

    def getPeso(self):
        return self._peso

    def getDimensiones(self):
        return self._dimensiones

    def getCosto(self):
        return self._costo

    def getEstado(self):
        return self._estado

    def getEstadosEnvio(self):
        return self._estadosEnvio

    #Comandos de modificación
    def setRemitente(self, nuevoRemitente):
        self._remitente = nuevoRemitente

    def setDestinatario(self, nuevoDestinatario):
        self._destinatario = nuevoDestinatario

    def setPeso(self, nuevoPeso):
        self._peso = nuevoPeso

    def setDimensiones(self, nuevasDimensiones):
        self._dimensiones = nuevasDimensiones

    def setCosto(self, nuevoCosto):
        self._costo = nuevoCosto


    #Comandos de Operación
    def actualizarEstado(self, nuevoEstado):
        estados = ["Pendiente de despacho", "Despachado", "En viaje",
                   "Visita a domicilio", "Recibido", "Rechazado"]

        if nuevoEstado in estados:
            self._estado = nuevoEstado



