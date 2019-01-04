def raizCuadradaEcuacion(a, b, c):
    interiorRaiz = b ** 2 - 4 * a * c
    if interiorRaiz < 0:
        return None
    else:
        return round((interiorRaiz ** (1/2)), 2)


def dividendoEcuacion(a):
    if 2 * a == 0:
        return None
    else:
        return 2 * a


def raizPositiva(a, b, c):
    if raizCuadradaEcuacion(a, b, c) == None:
        return None
    else:
        divisor = -b + raizCuadradaEcuacion(a, b, c)
    if dividendoEcuacion(a) == None:
        return None
    else: 
        return round((divisor / dividendoEcuacion(a)), 2)


def raizNegativa(a, b, c):
    if raizCuadradaEcuacion(a, b, c) == None:
        return None
    else:
        divisor = -b - raizCuadradaEcuacion(a, b, c)
    if dividendoEcuacion(a) == None:
        return None
    else: 
        return round((divisor / dividendoEcuacion(a)), 2)


def raices(a, b, c):
    if raizPositiva(a, b, c) == None and raizNegativa(a, b, c) == None:
        return 'La ecuación no tiene soluciones reales'
    elif raizPositiva(a, b, c) == raizNegativa(a, b, c):
        return raizPositiva(a, b, c), 'Solución única'
    else:
        return raizPositiva(a, b, c), raizNegativa(a, b, c)


def obtencionListaConstantes(constantesString):
    constantesStringList = constantesString.split(',')
    constantes = []
    for numero in constantesStringList:
        constantes.append(float(numero))
    return constantes

constantesInput = input('Introduzca las constantes de la ecuación a resolver, separados por comas: ')
a = obtencionListaConstantes(constantesInput)[0]
b = obtencionListaConstantes(constantesInput)[1]
c = obtencionListaConstantes(constantesInput)[2]


print(raices(a, b, c))




##CASOS TEST
if __name__ == '__main__':
    assert raizPositiva( 1, -5, 6) == 3
    assert raizPositiva(2, -7, 3) == 3
    assert raizPositiva(1, -2, 1) == 1
    assert raizPositiva(1, 3, -4) == 1
    assert raizPositiva(1, 1, 1) == None

    assert raizNegativa(1, -5, 6) == 2
    assert raizNegativa(2, -7, 3) == 1 / 2
    assert raizNegativa(1, -2, 1) == 1
    assert raizNegativa(1, 3, -4) == -4
    assert raizNegativa(1, 1, 1) == None
    
    assert raices(1, -5, 6) == (3, 2)
    assert raices(2, -7, 3) == (3, 1 / 2)
    assert raices(1, -2, 1) == (1, 'Solución única')
    assert raices(1, 3, -4) == (1, -4)
    assert raices(1, 1, 1) == 'La ecuación no tiene soluciones reales'

     
