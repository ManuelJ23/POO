# Nombre y apellido: Manuel Jarque

class Fecha():
    #Constructor
    def __init__(self, dia, hora):
        self._dia = dia
        self._hora = hora

    #Métodos de consulta
    def getDia(self):
        return self._dia
    def getHora(self):
        return self._hora

    #Métodos de modificación
    def setDia(self, dia):
        self._dia = dia
    def setHora(self, hora):
        self._hora = hora

class Persona():
    #Constructor
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    #Métodos de consulta
    def getNombre(self):
        return self._nombre
    def getDni(self):
        return self._dni

    #Métodos de modificación
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDni(self, dni):
        self._dni = dni

    #Métodos operacionales
    def mostrarInformacion(self):
        return f"\tNombre: {self._nombre}, DNI: {self._dni}"

class Reglamento():
    #Constructor
    def __init__(self, diaNoPermitido, horaNoPermitida):
        self._diaNoPermitido = diaNoPermitido
        self._horaNoPermitida = horaNoPermitida

    #Métodos operacionales
    def habilitarReunion(self, dia, hora):
        if dia == self._diaNoPermitido or hora == self._horaNoPermitida:
            return False
        else:
            return True

    def consultarReglamento(self):
        print(f"No se permiten reuniones los días {self._diaNoPermitido}, ni reuniones que comiencen a las {self._horaNoPermitida} horas")

class Reunion():
    #Constructor
    def __init__(self, nombre, fecha):
        self._nombre = nombre
        self._fecha = fecha
        self._habilitada = False
        self._listaParticipantes = []

    #Métodos de consulta
    def getNombre(self):
        return self._nombre
    def getFecha(self):
        return self._fecha

    #Métodos de modificación
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDia(self, dia):
        self._dia = dia
    def setHora(self, hora):
        self._hora = hora

    #Métodos operacionales
    def solicitarHabilitacion(self, reglamento):
        self._habilitada = reglamento.habilitarReunion(self._fecha.getDia(), self._fecha.getHora())

    def reunionHabilitada(self):
        return self._habilitada

    def agregarParticipante(self, persona):
        if isinstance(persona, Persona):
            for participante in self._listaParticipantes:
                if participante.getDni() == persona.getDni():
                    print("No se pueden agregar participantes con el mismo DNI")
                    return
            self._listaParticipantes.append(persona)
        else:
            print("Error al cargar el participante.")

    def mostrarListaParticipantes(self):
        print("Lista de participantes: ")
        for participante in self._listaParticipantes:
            print(participante.mostrarInformacion())


