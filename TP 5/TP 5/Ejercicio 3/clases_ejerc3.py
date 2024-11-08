class Precio():
    def __init__(self, *args):
        self._valor = args[0]

        if len(args) == 1:
            if isinstance(args[0], int):
                self._valor = args[0]
                self._descuento = 0
                self._recargo = 0
            else:
                raise TypeError("El dato debe ser de tipo entero")

        elif isinstance(args[1], int):
            self._valor = args[0]
            self._descuento = args[1]
            self._recargo = 0

        elif isinstance(args[1], tuple):
            self._valor = args[0]
            self._descuento = args[1][0]
            self._recargo = args[1][1]
        else:
            raise TypeError ("Los tipos de datos no coinciden con lo esperado")

    def mostrarOpcionesPago(self):
        """Muestra las opciones de pago según el descuento y recargo aplicados."""
        mensaje = f"El precio de lista es ${self._valor} - "
        if self._descuento > 0:
            mensaje += f"Descuento de {self._descuento}% por pago efectivo - "
        else:
            mensaje += "No hay descuento por pago efectivo - "

        if self._recargo > 0:
            mensaje += f"Recargo de {self._recargo}% por pago en 3 cuotas"
        else:
            mensaje += "No hay opción de pago en cuotas"

        return mensaje

    def calcular_preco_efectivo(self):
        """Calcula el precio con descuento por pago en efectivo."""
        return self._valor * (1 - self._descuento / 100)

    def calcular_precio_cuotas(self):
        """Calcula el precio con recargo por pago en 3 cuotas."""
        return self._valor * (1 + self._recargo / 100)