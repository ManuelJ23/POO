from definicion_clases_ejerc1 import *

miTeclado  = Teclado("Logitech", "Español", True, False)
miMonitor = Monitor("Asus", 24, "LED", "AMBAS")

miComputadora = Computadora("Asus", 12, "I3 11gen", False, miTeclado, miMonitor)

#Accediendo a atributos propios de la clase Computadora

print(miComputadora.getMarca())
print(miComputadora.getMemoriaRam())

#Accediendo a atributos de los objetos atributos de la clase Computadora

print(miComputadora.getTeclado().getMarca())


#Modificando una clase desde otra
print(miComputadora.getTeclado().getIncluyeRetroIlum())
miComputadora.getTeclado().setIncluyeRetroIlum(True)
print(miComputadora.getTeclado().getIncluyeRetroIlum())









