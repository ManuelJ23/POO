from definicion_clases_ejerc2A import *

cliente1 = Cliente("Lara", ["Manteca", "Tomates", "Harina"], True)
cliente2 = Cliente("Manuel", ["Avena", "Banana", "Huevos"], True)

print(cliente1.getListaCompras())
cliente1.setListaCompras("Toallitas")
print(cliente1.getListaCompras())

comercio1 = Comercio("Cooperativa", "Guatemala 1051", "supermercado")


comercio1.agregarCliente(cliente2)
comercio1.agregarCliente(cliente1)
print(comercio1.getlistaClientes())

comercio1.despacharCliente()