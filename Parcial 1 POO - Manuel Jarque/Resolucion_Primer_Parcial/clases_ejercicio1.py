# Nombre y apellido: Manuel Jarque

class CuentaUsuario():
    #Constructor
    def __init__(self, nombreUsuario, email, contrasenia):
        self._nombreUsuario = nombreUsuario
        self._email = email
        self._contrasenia = contrasenia
        self._estadoSesion = False
        self._favoritos = []
        self._registroOperaciones = []

        self._registroOperaciones.append(f"Se creó una cuenta de usuario para {self._nombreUsuario}")


    #Métodos de consulta
    def getNombreUsuario(self):
        return self._nombreUsuario

    def getEmail(self):
        return self._email

    def getEstadoSesion(self):
        return self._estadoSesion
    

    #Métodos de modificación
    def setNombreUsuario(self, nuevoNombreUsuario):
        self._nombreUsuario = nuevoNombreUsuario


    #Métodos operacionales

    def verificarEmailValido(self):
        if "@" not in self._email:
            self._registroOperaciones.append(f"El email ingresado no es válido '{self._email}'")

    def modificarEmail(self, nuevoEmail):
        self._email = nuevoEmail
        self._registroOperaciones.append(f"Se modificó el email a '{nuevoEmail}'")

    def verFavoritos(self):
        self._registroOperaciones.append("Se visualizó la lista de favoritos.")
        return f"Favoritos: \n{self._favoritos}"

    def cambiarContrasenia(self, contraseniaActual, nuevaContrasenia):

        if isinstance(nuevaContrasenia, int):
            if self._contrasenia == contraseniaActual:
                self._contrasenia = nuevaContrasenia #Verificar si la contra es instancia de int
                self._registroOperaciones.append("Se modificó la contraseña correctamente.")
            else:
                self._registroOperaciones.append("No se pudo modificar la contraseña porque no coincide con la contraseña actual")
        else:
            self._registroOperaciones.append("No se pudo modificar la contraseña ya que no coincide con el formato requerido")


    def consultarDatos(self):
        datos_usuario = {
            "Nombre" : self._nombreUsuario,
            "Email" : self._email
        }
        self._registroOperaciones.append(f"Se consultaron los datos de la cuenta de '{self._nombreUsuario}'")
        return datos_usuario

    def mostrarRegistroOperaciones(self):
        for operacion in self._registroOperaciones:
            print(f"\n{operacion}")

    def enviarMensaje(self, emailDestino, mensaje):
        if isinstance(emailDestino, str) and isinstance(mensaje, str):
            if "@" not in self._email:
                self._registroOperaciones.append("No se puede enviar un mensaje porque el email no es válido")
            elif "@" not in emailDestino:
                self._registroOperaciones.append("No se puede enviar un mensaje porque el email de destino no es válido")
            else:
                self._registroOperaciones.append(f"Se envió un mensaje a '{emailDestino}'")
        else:
            self._registroOperaciones.append("Los datos ingresados no son válidos")


    def iniciarSesion(self, email, contrasenia):
        if not self._estadoSesion:
            if email == self._email and contrasenia == self._contrasenia:
                self._estadoSesion = True
                self._registroOperaciones.append("Sesión iniciada")
            else:
                self._registroOperaciones.append("Datos incorrectos. No se pudo iniciar sesión")
        else:
            self._registroOperaciones.append("La sesión ya está iniciada.")


    def cerrarSesion(self, nombreUsuario):
        if self._estadoSesion:
            if nombreUsuario == self._nombreUsuario:
                self._estadoSesion = False
                self._registroOperaciones.append("Cerrando sesión...")
            else:
                self._registroOperaciones.append("El nombre de usuario no coincide.")
        else:
             self._registroOperaciones.append("La sesión no está iniciada.")


    #Método adicional

    def agregarAFavoritos(self, email):
        if "@" not in email:
            self._registroOperaciones.append("No se puede agregar a favoritos el email porque no es válido.")
        else:
            self._favoritos.append(email)
            self._registroOperaciones.append(f"Se agregó exitosamente a favoritos el email '{email}'")
