# Manuel Jarque

class Contacto:
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono
    
    def getInfo(self):
        return f"Nombre: {self._nombre} - Número de Teléfono: {self._telefono}"

    def getNombre(self):
        return self._nombre

    def getTelefono(self):
        return self._telefono
    
    def __lt__(self, other):
        if isinstance(self, Contacto) and isinstance(other, Contacto):
            return self._telefono < other.getTelefono()
    
class Agenda:
    def __init__(self, nombre):
        self._nombre = nombre
        self._listaContactos = []
        
    def agregarContacto(self, contacto):
        if isinstance(contacto, Contacto):
            if contacto not in self._listaContactos:
                self._listaContactos.append(contacto)
    
    def getNombre(self):
        return self._nombre

    def getListaContactos(self):
        return self._listaContactos

    def setListaContactos(self, nuevoListaContactos):
        self._listaContactos = nuevoListaContactos

    def __add__(self, other):
        if isinstance(self, Agenda) and isinstance(other, Agenda):
            nuevoNombre = f"{self._nombre} y {other.getNombre()}"
            agenda = Agenda(nuevoNombre)
            nuevaLista = self._listaContactos + other.getListaContactos()
            agenda.setListaContactos(nuevaLista)
            return agenda

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx < len(self._listaContactos):
            contacto = self._listaContactos[self._idx]
            self._idx += 1
            return contacto.getNombre()
        else:
            raise StopIteration