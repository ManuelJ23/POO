from clase_caja import *

caja1 = Caja("Madera", 12, 30, 40)
print(caja1)

cajaChica = Caja.cajaChica("Cartón")
print(cajaChica)

cajaGrande = Caja.cajaGrande("Cartón")
print(cajaGrande)

cajaCarton = Caja.cajaCarton(12,30, 40)
print(cajaCarton)

cajaPlastica = Caja.cajaPlastica(12, 30, 40)
print(cajaPlastica)

cajaFuerte = Caja.cajaFuerte()
print(cajaFuerte)

cajaRegalo = Caja.cajaRegalo(12, 30, 40)
print(cajaRegalo)

print(Caja.entraONo(cajaGrande))
print(Caja.entraONo(cajaChica))
