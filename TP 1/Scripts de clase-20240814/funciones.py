def ampliar(valor, escala = 2):
    """
    Amplia un valor recibido como parámetro por una escala dada con valor por defecto 2.

    :param valor: int - El valor que se desea ampliar
    :param escala: int (default = 2) - La escala por la cual se amplia el valor
    :return: int - El valor ampliado

    Examples
    --------
    >>> ampliar(10)
    20
    >>> ampliar(10, 3)
    30
    """

    return valor * escala

