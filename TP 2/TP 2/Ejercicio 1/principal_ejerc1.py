from clases_ejerc1 import *

miMonitor = Monitor("Asus", 22,"FULL HD LED", "HDMI")

print(f"Mi monitor es de la marca {miMonitor.getMarca()}, tiene una resolución de {miMonitor.getTamanio()}, su tipo de pantalla es {miMonitor.getTipoPantalla()} y su tipo de conexión es {miMonitor.getTipoConexion()}")

Monitor.setMarca(miMonitor, "Samsung")

print(f"Mi monitor es de la marca {miMonitor.getMarca()}, tiene una resolución de {miMonitor.getTamanio()}, su tipo de pantalla es {miMonitor.getTipoPantalla()} y su tipo de conexión es {miMonitor.getTipoConexion()}")


miTeclado = Teclado("Razer", "Español", False, True)

print(f"Mi teclado es de la marca {miTeclado.getMarca()}, su lenguaje es {miTeclado.getLenguaje()}, {miTeclado.getIncluyeNumPad()} incluye NumPad y {miTeclado.getIncluyeRetroIlum()} incluye RetroIluminación.")

Teclado.setIncluyeNumPad(miTeclado, True)

print(f"Mi teclado es de la marca {miTeclado.getMarca()}, su lenguaje es {miTeclado.getLenguaje()}, {miTeclado.getIncluyeNumPad()} incluye NumPad y {miTeclado.getIncluyeRetroIlum()} incluye RetroIluminación.")





