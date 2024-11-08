class Vector():

    # Constructor

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, nuevoX):
        self._x = nuevoX

    def setY(self, nuevoY):
        self._y = nuevoY

    def __str__(self):
        return f"Vector = (x : {self._x}, y : {self._y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            sumax = self._x + other.getX()
            sumay = self._y + other.getY()
            return Vector(sumax, sumay)

        if isinstance(other, int):
            sumax = self._x + other
            sumay = self._y + other
            return Vector(sumax, sumay)

    def __radd__(self, other):
        if isinstance(other, int):
            sumax = self._x + other
            sumay = self._y + other
            return Vector(sumax, sumay)

    def __rmul__(self, other):
        if isinstance(other, int):
            mx = self._x * other
            my = self._y * other
            return Vector(mx, my)

    def __iter__(self):
        self._idx = 0
        self._valores = [self._x, self._y]
        return self

    def __next__(self):
        if self._idx < len(self._valores):
            elemento = self._valores[self._idx]
            self._idx += 1
            return elemento
        else:
            raise StopIteration

    def __sub__(self, other):
        if isinstance(other, Vector):
            subx = self._x - other.getX()
            suby = self._y  - other.getY()
            return Vector(subx, suby)

    def __len__(self):
        return 2

    def invertir(self):
        xinv = -1 * self._x
        yinv = -1 * self._y
        return Vector(xinv, yinv)
        