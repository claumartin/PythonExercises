
## 14. Pedir por teclado una cantidad de dinero.
# Mostrar la descomposición de dicho importe en el menor número de billetes y monedas de 100, 50, 20, 10, 5, 2 y 1 	euro. 
# Para una cantidad de 2236 euros la salida que generaría el programa sería:
#     22 billetes de 100 euros
#     1 billete de 20 euros
#     1 billete de 10 euros
#     1 billete de 5 euros
#     1 moneda de 1 euro

miCantidad = input('Introduzca el importe a descomponer ')

def descomposicionEfectivo(importe):
    caja = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
    resto = float(importe)
    while resto != 0:
        if resto >= 100:
            caja['100'] = int(resto / 100)
            resto = resto % 100
        elif resto < 100 and resto >= 50:
            caja['50'] = int(resto / 50)
            resto = resto % 50
        elif resto < 50 and resto >= 20:
            caja['20'] = int(resto / 20)
            resto = resto % 20
        elif resto < 20 and resto >= 10:
            caja['10'] = int(resto / 10)
            resto = resto % 10
        elif resto < 10 and resto >= 5:
            caja['5'] = int(resto / 5)
            resto = resto % 5
        elif resto < 5 and resto >= 2:
            caja['2'] = int(resto / 2)
            resto = resto % 2
        else:
            caja['1'] = int(resto)
            resto = 0
    
    resultado = ''
    for index, moneda in enumerate(caja):
        if index < 5:
            if caja[moneda] > 1:
                resultado = resultado + str(caja[moneda]) + ' billetes de ' + moneda + ' euros' + '\n'
            elif caja[moneda] == 1:
                resultado = resultado + str(caja[moneda]) + ' billete de ' + moneda + ' euros' + '\n'
        elif index == 5:
            if caja[moneda] > 1:
                resultado = resultado + str(caja[moneda]) + ' monedas de ' + moneda + ' euros' + '\n'
            elif caja[moneda] == 1:
                resultado = resultado + str(caja[moneda]) + ' moneda de ' + moneda + ' euros' + '\n'
        else:
            if caja[moneda] >= 1:
                resultado = resultado + str(caja[moneda]) + ' moneda de ' + moneda + ' euro' + '\n'
    return resultado
    print(resultado)

print(descomposicionEfectivo(miCantidad))




## CASOS TEST
if __name__ == '__main__':

    # Ejercicio 14
    assert descomposicionEfectivo(40) == '2 billetes de 20 euros\n'
    assert descomposicionEfectivo(71) == '1 billete de 50 euros\n1 billete de 20 euros\n1 moneda de 1 euro\n'
    assert descomposicionEfectivo(195) == '1 billete de 100 euros\n1 billete de 50 euros\n2 billetes de 20 euros\n1 billete de 5 euros\n'
    assert descomposicionEfectivo(207) == '2 billetes de 100 euros\n1 billete de 5 euros\n1 moneda de 2 euros\n'
    assert descomposicionEfectivo(2236) == '22 billetes de 100 euros\n1 billete de 20 euros\n1 billete de 10 euros\n1 billete de 5 euros\n1 moneda de 1 euro\n'