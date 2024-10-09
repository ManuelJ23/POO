def contieneCifra(numero,digito):
    contiene = False
    numeroStr = str(numero)
    digitoStr = str(digito)
    if digitoStr in numeroStr:
        contiene = True
    return contiene

def mayorDeDosNumerosReales(numero1,numero2):
    if numero1 > numero2:
        elMayor = numero1
    else:
        elMayor = numero2
    return elMayor

def mayorDeTresNumerosReales(numero1,numero2,numero3):
    elMayor = mayorDeDosNumerosReales(numero1,numero2)
    elMayor = mayorDeDosNumerosReales(elMayor,numero3)
    return elMayor


print(mayorDeDosNumerosReales(5,5))
print(mayorDeTresNumerosReales(30,6,10))
print(contieneCifra(123,5))