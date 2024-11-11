from clases_ejerc1 import *

jugador1 = Jugador("Juan")
jugador1.setLesionado(True)
jugador2 = Jugador("Carlos")
equipo1 = EquipoBasquet("TeamTeam")


# Caso 1: Verificar TypeError para tipo incorrecto
try:
    equipo1.agregarJugador("NoJugador", 6)
except TypeError as ex:
    print(ex)


# Caso 2: Verificar JugadorLesionadoError para jugador lesionado
try:
    equipo1.agregarJugador(jugador1, 6)
except JugadorLesionadoError as ex:
    nombreJugador = ex.args[0]
    print(f"Error: el jugador {nombreJugador} está lesionado y no puede jugar el partido.")


# Caso 3: Verificar CamisetaEnUsoError para número de camiseta en uso
try:
    equipo1.agregarJugador(jugador2, 6)
    equipo1.agregarJugador(jugador2, 6)
except CamisetaEnUsoError as ex:
    nroCamiseta = ex.args[0]
    print(f"Error: la camiseta N°{nroCamiseta} está en uso.")
