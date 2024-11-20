# Nombre y apellido
from ejercicio1 import *

# NO MODIFICAR LA CREACION DE LA LISTA NI EL PRIMER TEMA AGREGADO
lista1 = ListaDeReproduccion("Folklore")
lista1.agregarTema("Luna Tucumana", "Folklore")

# CASO 1 -----------------------------------------------------------
try:
    lista1.agregarTema("City of Stars", 123)
except TypeError as ex:
    print(ex)

# Mensaje a mostrar: "TypeError: el género de la canción debe ser de tipo str"


# CASO 2 -----------------------------------------------------------
try:
    lista1.agregarTema("Luna Tucumana", "Folklore")
except ValueError as ex:
    print(ex)
# # Mensaje a mostrar: "ValueError: el tema Luna Tucumana ya estaba en la lista"
#
#
# # CASO 3 -----------------------------------------------------------
try:
    lista1.agregarTema("Till I Collapse", "Rap")
except ValueError as ex:
    print(ex)
# # Mensaje a mostrar: "ValueError: la lista solo puede tener temas de Folklore"
#
#
# # CASO 4 -----------------------------------------------------------
# # Se agregan 4 temas más para alcanzar el máximo (NO MODIFICAR)
lista1.agregarTema("Los 60 Granaderos", "Folklore")
lista1.agregarTema("Recuerdos del Portezuelo", "Folklore")
lista1.agregarTema("Canción de Otoño", "Folklore")
lista1.agregarTema("Zamba de Abril", "Folklore")
#
try:
    lista1.agregarTema("Payador y de Dorrego", "Folklore")
except LimiteTemasError as ex:
    cantidadMaximaTemas = ex.args[0]
    print(f"La cantidad máxima de temas en la lista es {cantidadMaximaTemas}")
# Mensaje a mostrar: "LimiteTemasError: la cantidad máxima de temas en la lista es 5"

# CASO 5 -----------------------------------------------------------
# Definir una condición adicional para lanzar otra excepción personalizada (a elección)

#Cree una lista nueva porque sino no podía probar la excepción ya que antes se lanzaba la de CantidadMaximaTemas
lista2 = ListaDeReproduccion("Rock")

try:
    lista2.agregarTema("Esta canción tiene un nombre muy largooooooooooo", "Rock")
except NombreTemaLargoError as ex:
    nombre = ex.args[0]
    print(f"El nombre del tema '{nombre}' es muy largo. debe tener 25 caracteres como máximo.")