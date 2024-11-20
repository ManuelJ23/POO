# Nombre y apellido: Manuel Jarque

from clases_ejercicio2 import *

# Códigos de prueba del ejercicio 2

fechaReunion = Fecha("Jueves", 10)
fechaOtraReunion = Fecha("Sábado", 8)

reglamento = Reglamento("Sábado", 8)

miReunion = Reunion("Reunión para evaluar costos", fechaReunion)
otraReunion = Reunion("Reunion Contra las reglas", fechaOtraReunion)

miReunion.solicitarHabilitacion(reglamento)
print(miReunion.reunionHabilitada())
otraReunion.solicitarHabilitacion(reglamento)
print(otraReunion.reunionHabilitada())

persona1 = Persona("Manuel Jarque", 45461413)
persona2 = Persona("Lara Sensini", 45188520)
persona3 = Persona("Romina Copló", 45188520)
persona4 = 12


miReunion.agregarParticipante(persona1)
miReunion.agregarParticipante(persona2)
miReunion.agregarParticipante(persona3)
miReunion.agregarParticipante(persona4)

miReunion.mostrarListaParticipantes()