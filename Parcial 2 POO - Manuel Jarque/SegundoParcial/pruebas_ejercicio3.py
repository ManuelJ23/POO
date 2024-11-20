# Manuel Jarque
from ejercicio3 import *
#Partido de Voley
partidoVoley = PartidoVoley("Voleibol",6,"mejor de 5 sets","madera","Los Soles", "Las Nubes")

print(partidoVoley.detallarJuego())

print(partidoVoley.mostrarEquipos())

partidoVoley.puntosDelPartido(25, 20)  # Gana Equipo A
partidoVoley.puntosDelPartido(18, 25)  # Gana Equipo B
partidoVoley.puntosDelPartido(25, 15)  # Gana Equipo A
partidoVoley.puntosDelPartido(22, 25)  # Gana Equipo B
partidoVoley.puntosDelPartido(15, 10)  # Gana Equipo A y termina el partido

print()

###############################################
#Partido de Fútbol"
partidoFutbol = PartidoFutbol("Fútbol",11,"Tiempo reglamentario","Césped","Las Lunas","Las Estrellas")

# Detallar el juego (sin goles)
print(partidoFutbol.detallarJuego())

# Probar con goles por minuto (Caso 1)

partidoFutbol.golesDelPartido(30, 52, 77)


# Probar con goles en una lista con equipo (Caso 2)

partidoFutbol.golesDelPartido([[30, 'V'], [52, 'L'], [77, 'L']])


# Probar con el marcador progresivo (Caso 3)

partidoFutbol.golesDelPartido((0, 0), (0, 1), (1, 1), (2, 1))

print()
###############################################
#Ejemplo de Polimorfismo

listaPartidos = [partidoVoley, partidoFutbol]
for partido in listaPartidos:
    print(partido.verificarResultado())

#Dado que el polimorfismo nos permite tratar objetos distintos como
#instancias de una misma clase base, acá lo usé para imprimir los
#resultados de partidos de distintos deportes, ya que comparten
#el método abstracto "verificarResultado" porque lo heredaron de la misma
#clase padre "JuegoEnCancha", y lo sobreescribieron según necesidad.