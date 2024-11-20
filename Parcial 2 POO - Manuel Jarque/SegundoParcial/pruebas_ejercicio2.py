# Manuel Jarque
from ejercicio2 import *

# Crear tres contactos ***************************************************
# (modificar el código)
contacto1 = Contacto("Rita", 2915221583)
contacto2 = Contacto("Maru", 2983385317)
contacto3 = Contacto("Juan", 2922509351)

# Comparar teléfonos de dos contactos *************************************
# (NO modificar el código, completar implementación de las clases)
if contacto1 < contacto2:
    print('El número de teléfono del contacto1 es menor al del contacto2')
else:
    print('El número de teléfono del contacto1 no es menor al del contacto2')

# Crear dos agendas *****************************************************
# (modificar el código)
agendaPersonal = Agenda("Agenda Personal")
agendaLaboral = Agenda("Agenda Laboral")

# Agregar los contactos 1 y 2 a la agendaPersonal ***********************
agendaPersonal.agregarContacto(contacto1)
agendaPersonal.agregarContacto(contacto2)


# Agregar el contacto 3 a la agendaLaboral ******************************
agendaLaboral.agregarContacto(contacto3)


# Crear una agenda completa *********************************************
# El nombre de la nueva agenda debe ser la concatenación del nombre de ambas
# (NO modificar el código, completar implementación de las clases)

agendaCompleta = agendaLaboral + agendaPersonal

# Mostrar los nombres de los contactos agendados ************************
# (NO modificar el código, completar implementación de las clases)
for nombre in agendaCompleta:
    print("Nombre del contacto:", nombre)
