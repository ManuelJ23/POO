from clases_ejerc3 import *

miEncomienda = Encomienda("Manuel Jarque", "Carlos Caceres", 1.5, [20, 30, 10], 3500)

print(f"Remitente: {miEncomienda.getRemitente()} \nDestinatario: {miEncomienda.getDestinatario()} \nPeso (KG): {miEncomienda.getPeso()} \nDimensiones (CM): {miEncomienda.getDimensiones()} \nCosto: {miEncomienda.getCosto()} \nEstado: {miEncomienda.getEstado()}")


miEncomienda.setCosto(5000)
print(f"\nNuevo costo: {miEncomienda.getCosto()}")
miEncomienda.actualizarEstado("Todavía no llegó")
print(f"Nuevo estado: {miEncomienda.getEstado()}") #No tendría que cambiar
print(f"Posibles estados: {miEncomienda.getEstadosEnvio()}\n")
miEncomienda.actualizarEstado("En viaje")
print(f"Nuevo estado: {miEncomienda.getEstado()}\n") #Acá sí

print(f"Remitente: {miEncomienda.getRemitente()} \nDestinatario: {miEncomienda.getDestinatario()} \nPeso (KG): {miEncomienda.getPeso()} \nDimensiones (CM): {miEncomienda.getDimensiones()} \nCosto: {miEncomienda.getCosto()} \nEstado: {miEncomienda.getEstado()}")
