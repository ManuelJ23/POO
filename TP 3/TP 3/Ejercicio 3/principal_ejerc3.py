from definicion_clases_ejerc3 import *

miImpresora = Impresora("HP", "5600gf")
miArchivo = Archivo("Teta", 69, "Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta\nTeta Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta\nTeta Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta\nTeta Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta\nTeta Teta Teta Teta Teta Teta Teta Teta Teta Teta Teta\n")
noArchivo = "Teta"

miImpresora.encender()
miImpresora.imprimirArchivo(noArchivo)
miImpresora.imprimirArchivo(miArchivo)