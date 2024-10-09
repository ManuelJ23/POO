class Cliente:
    def __init__(self, nombreCliente, listaCompras, fiado):
        self._nombreCliente = nombreCliente
        self._listaCompras = listaCompras
        self._fiado = fiado


    def setNombreCliente(self, nuevo):
        self._nombreCliente = nuevo

    def getNombreCliente(self):
        return self._nombreCliente

    def setListaCompras(self, nuevo):
        self._listaCompras.append(nuevo) #Tendría que ser un comando operacional ya que hace más que asignar un valor nuevo a una variable

    def getListaCompras(self):
        return self._listaCompras

    def setFiado(self, nuevo):
        self._fiado = nuevo

    def getFiado(self):
        return self._fiado

class Comercio:
    def __init__(self, nombreComercio, direccion, rubro):
        self._nombreComercio = nombreComercio
        self._direccion = direccion
        self._rubro = rubro
        self._listaClientes = []

    def setnombreComercio(self, nuevo):
        self._nombreComercio = nuevo

    def getnombreComercio(self):
        return self._nombreComercio

    def setDireccion(self, nuevo):
        self._direccion = nuevo

    def getDireccion(self):
        return self._direccion

    def setRubro(self, nuevo):
        self._rubro = nuevo

    def getRubro(self):
        return self._rubro

    def agregarCliente(self, nuevo):
        self._listaClientes.append(Cliente)
        #Podria verificar si es instancia pero alta paja, estoy repasando conceptos
    def getlistaClientes(self):
        return self._listaClientes

    def despacharCliente(self):
        self._listaClientes.pop(0) #Verificar la longitud, si está vacía y demás. El primero que llega es el primero que se va