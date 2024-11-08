from clases_ejerc3 import *

p1 = Precio(1000)
p2 = Precio(1000, 10)
p3 = Precio(1000, (10, 25))

print(p1.mostrarOpcionesPago())
print(p2.mostrarOpcionesPago())
print(p3.mostrarOpcionesPago())