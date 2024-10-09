from clases_ejerc2 import *

miLibro = Libro("Viktor Frankl", "El hombre en búsqueda de sentido", "Psicología", 168)

print(f"Autor: {miLibro.getAutor()} \nTítulo: {miLibro.getTitulo()} \nGénero: {miLibro.getGenero()} \nCantidad de Páginas: {miLibro.getCantidadPaginas()}\n")

miOtroLibro = Libro("James Clear", "Hábitos Atómicos", "Estilo de vida", 326)

print(miOtroLibro.equals(miLibro)) #Debería dar False

miOtroLibro.copy(miLibro) #Debería copiar miLibro en miOtroLibro
print(f"\nAutor: {miLibro.getAutor()} \nTítulo: {miLibro.getTitulo()} \nGénero: {miLibro.getGenero()} \nCantidad de Páginas: {miLibro.getCantidadPaginas()}\n")
print(f"Autor: {miOtroLibro.getAutor()} \nTítulo: {miOtroLibro.getTitulo()} \nGénero: {miOtroLibro.getGenero()} \nCantidad de Páginas: {miOtroLibro.getCantidadPaginas()}\n")

miOtroLibro = Libro("James Clear", "Hábitos Atómicos", "Estilo de vida", 326)
miUltimoLibro = miOtroLibro.clone() #Debería generar objeto nuevo igual a miOtroLibro
print(f"Autor: {miUltimoLibro.getAutor()} \nTítulo: {miUltimoLibro.getTitulo()} \nGénero: {miUltimoLibro.getGenero()} \nCantidad de Páginas: {miUltimoLibro.getCantidadPaginas()}\n")
