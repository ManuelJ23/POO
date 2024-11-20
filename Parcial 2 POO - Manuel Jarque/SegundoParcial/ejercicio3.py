# Manuel Jarque
import random
from abc import ABC, abstractmethod


# NO MODIFICAR LA CLASE JuegoDeEquipos
class JuegoDeEquipos(ABC):
    def __init__(self, nombre, jugadoresPorEquipo, finalizaPor):
        self._nombre = nombre
        self._jugadoresPorEquipo = jugadoresPorEquipo
        self._finalizaPor = finalizaPor

    def detallarJuego(self):
        return f"Un juego de {self._nombre} se juega en equipos de {self._jugadoresPorEquipo}. El juego finaliza por {self._finalizaPor}"

    @abstractmethod
    def mostrarEquipos(self):
        pass


# COMPLETAR LA IMPLEMENTACION DE LAS CLASES FALTANTES

class JuegoEnCancha(JuegoDeEquipos, ABC):
    def __init__(self, nombre, jugadoresPorEquipo, finalizaPor, tipoPiso):
        super().__init__(nombre, jugadoresPorEquipo, finalizaPor)
        self._tipoPiso = tipoPiso

    def detallarJuego(self):
        cadena = super().detallarJuego()
        return cadena + f" y se juega en piso de {self._tipoPiso}."

    @abstractmethod
    def verificarResultado(self):
        pass

class PartidoVoley(JuegoEnCancha):
    def __init__(self, nombre, jugadoresPorEquipo, finalizaPor, tipoPiso, nombreLocal, nombreVisitante):
        super().__init__(nombre, jugadoresPorEquipo, finalizaPor, tipoPiso)
        self._nombreLocal = nombreLocal
        self._nombreVisitante = nombreVisitante
        self._marcador = [0, 0]
        self._puntosPorSet = []

    def detallarJuego(self):
        cadena = super().detallarJuego()
        return cadena + f" El nombre del equipo Local es {self._nombreLocal}, mientras que el visitante se llama {self._nombreVisitante}. En sets van {self._marcador} y en puntos del set {self._puntosPorSet}."

    def mostrarEquipos(self):
        return f"Equipo Local: {self._nombreLocal} - Equipo Visitante: {self._nombreVisitante}"

    def verificarResultado(self):
        # Un equipo gana cuando tiene 3 sets
        if self._marcador[0] == 3:
            return f"El equipo '{self._nombreLocal}' ha ganado el partido"
        elif self._marcador[1] == 3:
            return f"El equipo '{self._nombreVisitante}' ha ganado el partido"
        else:
            return "El partido continúa"

    def puntosDelPartido(self, puntosLocal, puntosVisitante):
        # Agregar los puntos de este set a la lista de sets
        self._puntosPorSet.append((puntosLocal, puntosVisitante))

        # Determinar el ganador del set y actualizar el marcador en sets
        if puntosLocal > puntosVisitante:
            self._marcador[0] += 1
        elif puntosVisitante > puntosLocal:
            self._marcador[1] += 1

        # Imprimir el resultado del set
        print(f"Resultado del set: {self._nombreLocal}: {puntosLocal} - {self._nombreVisitante}: {puntosVisitante}")



class PartidoFutbol(JuegoEnCancha):
    def __init__(self, nombre, jugadoresPorEquipo, finalizaPor, tipoPiso, nombreLocal, nombreVisitante):
        super().__init__(nombre, jugadoresPorEquipo, finalizaPor, tipoPiso)
        self._nombreLocal = nombreLocal
        self._nombreVisitante = nombreVisitante
        self._marcador = (0, 0)

    def detallarJuego(self):
        cadena = super().detallarJuego()
        return cadena + f" El nombre del equipo Local es {self._nombreLocal}, mientras que el visitante se llama {self._nombreVisitante}. El marcador esta {self._marcador}"

    def mostrarEquipos(self):
        return f"Equipo Local: {self._nombreLocal} - Equipo Visitante: {self._nombreVisitante}"

    def golesDelPartido(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            # Caso 2: Lista de goles con equipo
            goles = args[0]
            self._goles = goles
            resultado = []
            marcador_local, marcador_visitante = 0, 0

            for minuto, equipo in goles:
                if equipo == 'L':
                    resultado.append(f"Local a los {minuto}min")
                    marcador_local += 1
                elif equipo == 'V':
                    resultado.append(f"Visitante a los {minuto}min")
                    marcador_visitante += 1

            self._marcador = (marcador_local, marcador_visitante)
            print("Goles del partido:", " - ".join(resultado))

        elif len(args) > 1 and isinstance(args[0], tuple):
            # Caso 3: Marcador progresivo
            self._goles = args
            resultado = [f"{gol[0]}-{gol[1]}" for gol in args] #Esto lo hice sólo para formatear los goles, pero podría haberlo hecho más simple sin esto
            self._marcador = args[-1]  # Actualizar al marcador final
            print("El marcador del partido fue", ", ".join(resultado))

        # elif len(args) > 1 and isinstance(args[0], tuple):
        #     goles = args
        #     self._marcador = goles[-1]
        #     print(f"El marcador del partido fue {goles}")

        else:
            # Caso 1: Lista de minutos
            minutos = args
            resultado = ""
            for i, minuto in enumerate(minutos): #Ver que funcion tiene esto
                if i == len(minutos) - 1:
                    resultado += f"y {minuto} "
                else:
                    resultado += f"{minuto}, "
            print("Los goles del partido fueron a los", resultado.strip(", "), "minutos") #No se porque puse el strip, porque técnicamente se imprime el mismo resultado

    def verificarResultado(self):
        # Evaluar si hay empate o victoria de algún equipo
        if self._marcador[0] > self._marcador[1]:
            return f"El equipo '{self._nombreLocal}' ha ganado el partido"
        elif self._marcador[0] < self._marcador[1]:
            return f"El equipo '{self._nombreVisitante}' ha ganado el partido"
        else:
            return "El partido ha terminado en empate"
