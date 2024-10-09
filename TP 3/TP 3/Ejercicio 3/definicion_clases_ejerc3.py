class Impresora():
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._estaEncendida = False


    def setMarca(self, nuevo):
        self._marca = nuevo

    def getMarca(self):
        return self._marca

    def setModelo(self, nuevo):
        self._modelo = nuevo

    def getModelo(self):
        return self._modelo

    def getEstado(self):
        return self._estaEncendida

    def encender(self):
        self._estaEncendida = True

    def apagar(self):
        self._estaEncendida = False

    def imprimirArchivo(self, archivo):
        if self._estaEncendida:
            if isinstance(archivo, Archivo):
                print(f"\nImprimiendo '{archivo.getTitulo()}' ({archivo.getCantidadPaginas()} páginas)...")
                print(f"\nContenido: {archivo.getContenido()}")
                print("Impresión Completada.")
            else:
                print("El archivo no tiene el formato válido para imprimirse.\n")
        else:
            print("La impresora está apagada. No es posible imprimir el archivo\n")


class Archivo():
    def __init__(self, titulo, cantidadPaginas, contenido):
        self._titulo = titulo
        self._cantidadPaginas = cantidadPaginas
        self._contenido = contenido


    def setTitulo(self, nuevo):
        self._titulo = nuevo

    def getTitulo(self):
        return self._titulo


    def setCantidadPaginas(self, nuevo):
        self._cantidadPaginas = nuevo

    def getCantidadPaginas(self):
        return self._cantidadPaginas

    def setContenido(self, nuevo):
        self._contenido = nuevo

    def getContenido(self):
        return self._contenido



