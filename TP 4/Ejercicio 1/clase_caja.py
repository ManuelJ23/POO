class Caja():

    # Método estático

    @staticmethod
    def entraONo(caja): # Se podría mejorar haciendo una clase estante o una lista con las medidas para que sea más dinámico, y no estén hardcodeadas las medidas
        if caja.getAncho() < 50 and caja.getLargo() < 40 and caja.getAlto() < 30:
            return "La caja entra en la estantería"
        return "La caja es muy grande para la estantería"

    #Constructor

    def __init__(self, material, ancho, largo, alto):
        self._material = material
        self._ancho = ancho
        self._largo = largo
        self._alto = alto

    def __repr__(self):
        return f"Caja({self._material}, {self._ancho}, {self._largo}, {self._alto})"

    #Setters y getters
    def setMaterial(self, nuevoMaterial):
        self._material = nuevoMaterial

    def getMaterial(self):
        return self._material

    def setAncho(self, nuevoAncho):
        self._ancho = nuevoAncho

    def getAncho(self):
        return self._ancho

    def setLargo(self, nuevoLargo):
        self._largo = nuevoLargo

    def getLargo(self):
        return self._largo

    def setAlto(self, nuevoAlto):
        self._alto = nuevoAlto

    def getAlto(self):
        return self._alto

    #Métodos de clase

    @classmethod
    def cajaGrande(cls, material):
        return cls(material, 60, 70, 80)

    @classmethod
    def cajaChica(cls, material):
        return cls(material, 6, 7, 8)

    @classmethod
    def cajaCarton(cls, ancho, largo, alto):
        return cls("Carton", ancho, largo, alto)

    @classmethod
    def cajaPlastica(cls, ancho, largo, alto):
        return cls("Plástico", ancho, largo, alto)

    @classmethod
    def cajaFuerte(cls):
        return cls("Metal", 10, 20, 15)

    @classmethod
    def cajaRegalo(cls, ancho, largo, alto):
        return cls("Papel Regalo", ancho, largo, alto)