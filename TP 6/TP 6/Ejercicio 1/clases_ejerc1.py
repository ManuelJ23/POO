class JugadorLesionadoError(Exception):
    def __init__(self, nombreJugador):
        self._nombreJugador = nombreJugador

class CamisetaEnUsoError(Exception):
    def __init__(self, nroCamiseta):
        self._nroCamiseta = nroCamiseta


class Jugador():
    def __init__(self, nombre):
        self._nombre = nombre
        self._lesionado = False

    def getNombre(self):
        return self._nombre

    def getLesionado(self):
        return self._lesionado
    
    def setLesionado(self, nuevoLesionado):
        self._lesionado = nuevoLesionado

class EquipoBasquet():
    def __init__(self, nombreEquipo):
        self._nombreEquipo = nombreEquipo
        self._listaJugadores = []


    def agregarJugador(self, jugador, nroCamiseta):
        if not isinstance(jugador, Jugador):
            raise TypeError("Error: el jugador debe de ser de tipo Jugador")
        if not isinstance(nroCamiseta, int):
            raise TypeError("Error: el número de la camiseta debe ser de tipo Entero")

        if jugador.getLesionado():
            raise JugadorLesionadoError(jugador.getNombre())

        for jugador, camiseta in self._listaJugadores:
            if camiseta == nroCamiseta:
                raise CamisetaEnUsoError(nroCamiseta)

        self._listaJugadores.append((jugador, nroCamiseta))
