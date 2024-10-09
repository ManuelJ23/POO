# def saludar(nombre):
#     print("Hola", nombre) # parámetros de print
#     print("Hola " + str(nombre)) # concatenacion
#     print(f"Hola {nombre}") # f-Strings
#     print("Hola {}".format(nombre)) # método format
#     print("Hola %s" % nombre) # operador %


"""
def saludar(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, su edad es {edad} años.")


saludar(nombre="maría", edad=30, apellido="gonzalez")
"""

# def sumar(*args):
#     resultado = 0
#     #for valor in args: # recorrido por elementos
#     #    resultado += valor
#     for i in range(len(args)): # recorrido por índices
#         resultado += args[i]
#     return resultado
#
#
# def sumarLista(lista):
#     resultado = 0
#     for valor in lista:
#         resultado += valor
#     return resultado
#
#
# suma3 = sumar(10, 20, 30)
# suma2 = sumar(10, 20)
# suma4 = sumar(1,2,3,4)
#
# suma5 = sumarLista([1,2,3,4,5])


# def saludar(**kwargs):
#     print(f"Hola {kwargs['nombre']}, su edad es {kwargs['edad']} años")
#
#
# saludar(nombre="Ana", edad=25, apellido="Perez")
# saludar(nombre="Ana", edad=25)
# saludar(nombre="Ana", edad=25, apellido="Perez", dni=12345678)


# def ampliar(valor, escala = 2):
#     return valor * escala
#
# print(ampliar(10))
# print(ampliar(20))
# print(ampliar(10, 3))

# def generarLista(primero, ultimo = 10):
#     lista = []
#     for i in range(primero, ultimo + 1):
#         lista.append(i)
#     return lista
#
# l1 = generarLista(4)
# print(l1)
# l2 = generarLista(4, 12)
# print(l2)
# l3 = generarLista(15)
# print(l3)
#
#
# for i in range(15, 10, -2):
#     print(i)


def extremos(lista):
    primero = lista[0]
    ultimo = lista[-1]
    return primero, ultimo



resultado = extremos([5,7,3,2,8,9])
print(resultado)
primero = resultado[0]
print(primero)

p, u = extremos([5,7,3,2,8,9])
print(p)
print(u)