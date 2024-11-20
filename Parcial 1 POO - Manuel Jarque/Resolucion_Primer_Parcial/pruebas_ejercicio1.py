# Nombre y apellido: Manuel Jarque

from clases_ejercicio1 import *

# Códigos de prueba del ejercicio 1

miUsuario = CuentaUsuario("Manuel Jarque", "manueljarque23gmail.com", 4422)
miUsuario.verificarEmailValido()
miUsuario.iniciarSesion("manueljarque23gmail.com", 4422)
miUsuario.iniciarSesion("manueljarque23gmail.com", 4422)
miUsuario.enviarMensaje("pepito@gmail.com", "hola pepe")
miUsuario.modificarEmail("manuelJarque23@gmail.com")
miUsuario.enviarMensaje("pepito@gmail.com", "hola pepe")
miUsuario.enviarMensaje("pepitogmail.com", "hola pepe")
miUsuario.enviarMensaje("pepito@gmail.com", 18)


miUsuario.cambiarContrasenia(4242, 2244)
miUsuario.cambiarContrasenia(4422, 2244)
miUsuario.cambiarContrasenia(4422, "contrasenia")

miUsuario.agregarAFavoritos("pepito@gmail.com")
miUsuario.agregarAFavoritos("rosa@gmail.com.ar")
print(miUsuario.verFavoritos())

miUsuario.cerrarSesion("Manuel Jarque")
miUsuario.cerrarSesion("Manuel Jarque")


miUsuario.mostrarRegistroOperaciones()

