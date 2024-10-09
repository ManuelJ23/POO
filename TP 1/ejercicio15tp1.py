#a. A partir de los coeficientes de la forma polinómica, implementar una función que genere
#una cadena de caracteres con la expresión correspondiente.
#Ejemplo: si a=2,b=4,c=5, generar la cadena “P(x)=2*x^2 + 4*x + 5”.
def mostrarPolinomio(a,b,c):
    polinomioStr = f'P(x)={a}*x^2 '
    if b>=0:
        polinomioStr = polinomioStr + f'+ {b}*x '
    else:
        polinomioStr = polinomioStr + f'- {abs(b)}*x '

    if c>=0:
        polinomioStr = polinomioStr + f'+ {c}'
    else:
        polinomioStr = polinomioStr + f'- {abs(c)}'

    return polinomioStr

print(mostrarPolinomio(2,4,5))

#b. A partir de los coeficientes de la forma polinómica, determinar si tiene raíces reales y en
#caso afirmativo calcularlas.
# si el discriminante es positivo ---> tiene dos raices reales
# si el discriminante es cero ---> las dos raices reales son iguales
# si el discriminante es negativo ---> no hay raices reales
def tieneRaicesReales(a,b,c):
    discriminante = b**2 - 4*a*c
    print(discriminante)
    if discriminante>=0:
        x1 = (-b + discriminante**(1/2))/(2*a)
        x2 = (-b - discriminante**(1/2))/(2*a)
        bandera = True
    else:
        x1 = 0
        x2 = 0
        bandera = False
    return x1,x2,bandera

x1, x2, bandera = tieneRaicesReales(-2,4,5)
if bandera == True:
    print(f'Las raices son {x1} y {x2}')
else:
    print('No tiene raices reales')

#d. Implementar una función que permita evaluar el polinomio en un valor de x dado.
def evaluarPunto(valorX,a,b,c):
    valorY = a*(valorX*valorX) + b*valorX + c
    return valorY

print(evaluarPunto(1,-2,4,5))
#d. Utilizando la función del inciso anterior, implementar un subprograma para determinar el
#punto x de un intervalo dado donde el polinomio toma el menor valor. Los extremos del
#intervalo [ xmin , xmax ] deben ser recibidos por parámetro, además de un parámetro
#adicional maxdif , que indicará la distancia entre dos puntos de evaluación consecutivos.
def elMenorDelRango(listaRango,maxdif,a,b,c):
    valorMinimoDeX = listaRango[0]
    valorMaximoDeX = listaRango[1]
    valorYMinimo = evaluarPunto(valorMinimoDeX, a, b, c)
    valorXParaYMin = valorMinimoDeX;
    for x in range(valorMinimoDeX,valorMaximoDeX+1,maxdif):
        y = evaluarPunto(x,a,b,c)
        if y < valorYMinimo:
            valorYMinimo = y
            valorXParaYMin = x
    return valorXParaYMin

print(elMenorDelRango([-1,4],1,-2,4,5))

