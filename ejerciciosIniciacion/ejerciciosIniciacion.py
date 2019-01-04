## 1. Pedir por teclado un entero con un mensaje oportuno. 
# Luego mostrar en pantalla el número leído, el doble del número leído y el triple del mismo.

numeroEscrito = input('Escribe un número entero')

print(numeroEscrito)

def dobleNumeroEntero(numero):
    return numero * 2
print(dobleNumeroEntero(numeroEscrito))

def tripleNumeroEntero(numero):
    return numero * 3
print(tripleNumeroEntero(numeroEscrito))


## 2. Pedir por teclado el radio de una circunferencia. 
# Calcular y mostrar por pantalla la longitud de la circunferencia y del área del círculo.

miRadio = input('Escribe el radio de una circumferencia')

def longitudCircumferencia(radio):
    return 2.0 * float(radio) * 3.14
print(longitudCircumferencia(miRadio))

def areaCirculo(radio):
    return 3.14 * float(radio) ** 2.0
print(areaCirculo(miRadio))


# 3. Ejercicio 2 utilizando una constante que representa el valor de PI.

miRadio = input('Escribe el radio de una circumferencia')

PI = 3.14
def longitudCircumferencia(radio):
    return 2.0 * float(radio) * PI
print(longitudCircumferencia(miRadio))

def areaCirculo(radio):
    return 3.14 * float(radio) ** PI
print(areaCirculo(miRadio))


## 4. Calcula el área de una finca rectangular en metros cuadrados, así como su perímetro exterior, también en metros.

def areaRectangulo(base, altura):
    return base * altura

def perimetroRectangulo(base, altura):
    return 2 * base + 2 * altura


## 5. Calcula lo que tiene que cobrar un empleado sabiendo que se le tiene que aplicar al sueldo una retención del 20%.

def sueldoAPercibir(sueldo):
    retencion = (sueldo * 20) / 100
    return sueldo - retencion


## 6. Pedir por teclado dos valores de tipo numérico que se han de guardar en sendas variables.
# Mostrar por pantalla el contenido de las variables una vez leídas, 
# y volver a mostrar su contenido una vez intercambiados sus valores.

numeroA = float(input('Introduzca un número'))
print('numeroA: ', numeroA)
numeroB = float(input('Introduzca un segundo número'))
print('numeroB: ', numeroB)

print('Intercambio de valores...')
auxiliar = numeroA
numeroA = numeroB
numeroB = auxiliar
print('numeroA: ', numeroA, 'numeroB: ', numeroB)


## 7. Pedir por teclado un número. Mostrar por pantalla si el número leído es positivo o negativo.
# Consideramos al número 0 positivo.

miNumero = float(input('Introduzca un número'))

def signoNumero(numero):
    if numero >= 0:
        return 'Es positivo'
    else:
        return 'Es negativo'

print(signoNumero(miNumero))


## 8. Pedir por teclado dos números y mostrar por pantalla uno de los dos mensajes siguientes en función de los números leídos: 
# a) El primer número <valor> es mayor que el segundo <valor>; 
# b) El primer número <valor> es menor que el segundo <valor>; 
# c) Los dos números son iguales <valor>.

numeroA = input('Introduzca un número')
numeroB = input('Introduzca un segundo número')

def relacionOrden(numeroA, numeroB):
    if float(numeroA) > float(numeroB):
        return 'El primer número ' + str(numeroA) + ' es mayor que el segundo ' + str(numeroB)
    elif float(numeroA) < float(numeroB):
        return 'El primer número ' + str(numeroA) + ' es menor que el segundo ' + str(numeroB)
    else:
        return 'Los dos números son iguales ' + str(numeroA)

print(relacionOrden(numeroA, numeroB))


## 9. Pedir por teclado dos números enteros y mostrar por pantalla la suma de los dos números solamente si son los dos positivos. 
# Si no se cumple que los dos números sean positivos, mostrar un mensaje indicándolo. 
# La salida ha de tener el siguiente formato: 
# 'La suma de los dos números es: XX' o 'No se calcula la suma porque alguno de los números o los dos no son positivos'.

numeroA = int(input('Introduzca un número entero'))
numeroB = int(input('Introduzca otro número entero'))

def suma(numeroA, numeroB):
    if numeroA < 0 or numeroB < 0:
        return 'No se calcula la suma porque alguno de los números o los dos no son positivos'
    else:
        return 'La suma de los dos números es: ' + str(numeroA + numeroB)
    
print(suma(numeroA, numeroB))


## 10. Variante ejercicio anterior.
#  Mostrar por pantalla algo distinto para cada una de las situaciones que se puedan producir, utilizando los siguientes mensajes:
# a. 'No se calcula la suma porque el primer número es negativo'
# b. 'No se calcula la suma porque el segundo número es negativo'
# c. 'No se calcula la suma porque los dos números son negativos'

numeroA = int(input('Introduzca un número entero'))
numeroB = int(input('Introduzca otro número entero'))

def suma(numeroA, numeroB):
    if numeroA < 0 and numeroB < 0:
        return 'No se calcula la suma porque los dos números son negativos'
    elif numeroA < 0:
        return 'No se calcula la suma porque el primer número es negativo'
    elif numeroB < 0:
        return 'No se calcula la suma porque el segundo número es negativo'
    else:
        return 'La suma de los dos números es: ' + str(numeroA + numeroB)
    
print(suma(numeroA, numeroB))


## 11. Pedir por teclado tres valores de tipo entero. 
# Calcular si se cumple que la suma de dos de ellos es igual al tercero. 
# La salida del programa tiene que tener el formato:
#   'Números introducidos: <N1>	<N2> <N3> (tabulador)'
# Y una de las cuatro líneas de salida siguientes:
#   'Se cumple que N1 = N2 + N3'
#   'Se cumple que N2 = N1 + N3'
#   'Se cumple que N3 = N1 + N2'
#   'Los números no se relacionan por suma y resultado'

numeroA = int(input('Introduzca el primer número entero'))
numeroB = int(input('Introduzca el segundo número entero'))
numeroC = int(input('Introduzca el tercer número entero'))

print('Números introducidos: ' + str(numeroA) + ' ' + str(numeroB) + ' ' + str(numeroC) + '\t')
def relacionSumaResultado(N1, N2, N3):
    if N1 == N2 + N3:
        return 'Se cumple que ' + str(N1) + ' ' + '= ' + str(N2) + ' ' + '+ ' + str(N3)
    elif N2 == N1 + N3:
        return 'Se cumple que ' + str(N2) + ' ' + '= ' + str(N1) + ' ' + '+ ' + str(N3)
    elif N3 == N1 + N2:
        return 'Se cumple que ' + str(N3) + ' ' + '= ' + str(N1) + ' ' + '+ ' + str(N2)
    else:
        return 'Los números no se relacionan por suma y resultado'

print(relacionSumaResultado(numeroA, numeroB, numeroC))


## 12. Pedir por teclado dos números. 
# Calcular y mostrar la suma solamente si:
#   a. los dos son pares 
#   b. el primero es menor que cincuenta 
#   c. y el segundo está dentro del intervalo cerrado 100-500. 
# En el caso de que no se cumplan las condiciones, en vez de la suma ha de visualizarse un mensaje de error.

numeroA = float(input('Introduzca el primer número'))
numeroB = float(input('Introduzca el segundo número'))

def sonPares(numeroA, numeroB):
    if numeroA % 2 == 0 and numeroB % 2 == 0:
        return True
    else:
        return False

def mayorQueCincuenta(numero):
    if numero > 50:
        return True
    else:
        return False

def entreCienYQuinientos(numero):
    if numero >= 100 and numero <= 500:
        return True
    else:
        return False

def sumaEnCondiciones(numeroA, numeroB):
    if sonPares(numeroA, numeroB) and mayorQueCincuenta(numeroA) and entreCienYQuinientos(numeroB):
        return numeroA + numeroB
    elif not sonPares(numeroA, numeroB):
        return 'Almenos uno de los números no es par'
    elif not mayorQueCincuenta(numeroA):
        return 'El primer número no es mayor que 50'
    elif not entreCienYQuinientos(numeroB):
        return 'El segundo número no está entre 100 y 500'

print(sumaEnCondiciones(numeroA, numeroB))


## 13. Calcular el importe final de una venta considerando que sobre el valor bruto se hace un descuento según la siguiente tabla:
#   a. Valores <=20 implican un descuento del 0%
#   b. Valores >20 y <=100 implican un descuento descuento del 5%
#   c. Valores >100 implican un descuento 10%

def descuento(valorBruto):
    if valorBruto <= 20:
        return 0
    elif valorBruto > 20 and valorBruto <= 100:
        return (valorBruto * 5) / 100
    else:
        return (valorBruto * 10) / 100

def importeFinal(valorBruto):
    return valorBruto - descuento(valorBruto)




## CASOS TEST
if __name__ == '__main__':
    
    # Ejercicio 1
    if isinstance(numeroEscrito, int):
        pass
    else:
        print('Los datos proporcionados son incorrectos')

    assert dobleNumeroEntero(2) == 4
    assert dobleNumeroEntero(8) == 16
    assert dobleNumeroEntero(50) == 100
    assert dobleNumeroEntero(3560) == 7120

    assert tripleNumeroEntero(2) == 6
    assert tripleNumeroEntero(8) == 24
    assert tripleNumeroEntero(50) == 150
    assert tripleNumeroEntero(3560) == 10680


    # Ejercicio 2
    if isinstance(miRadio, int) or isinstance(miRadio, float):
        pass
    else:
        print('Los datos proporcionados son incorrectos')
    
    assert longitudCircumferencia(2) == 12.56
    assert longitudCircumferencia(3.6) == 22.61
    assert longitudCircumferencia(11) == 69.08
    assert longitudCircumferencia(45.0) == 282.6

    assert areaCirculo(2) == 12.56
    assert areaCirculo(3.6) == 40.69
    assert areaCirculo(11) == 379.94
    assert areaCirculo(45.0) == 6358.5


    # Ejercicio 3
    if isinstance(miRadio, int) or isinstance(miRadio, float):
        pass
    else:
        print('Los datos proporcionados son incorrectos')
    
    assert longitudCircumferencia(2) == 12.56
    assert longitudCircumferencia(3.6) == 22.61
    assert longitudCircumferencia(11) == 69.08
    assert longitudCircumferencia(45.0) == 282.6

    assert areaCirculo(2) == 12.56
    assert areaCirculo(3.6) == 40.69
    assert areaCirculo(11) == 379.94
    assert areaCirculo(45.0) == 6358.5


    # Ejercicio 4
    assert areaRectangulo(2, 4) == 8
    assert areaRectangulo(2.0, 4.0) == 8.0
    assert areaRectangulo(5, 12) == 60
    assert areaRectangulo(15.4, 50.2) == 773.08

    assert perimetroRectangulo(2, 4) == 12
    assert perimetroRectangulo(2.0, 4.0) == 12.0
    assert perimetroRectangulo(5, 12) == 34
    assert perimetroRectangulo(15.4, 50.2) == 131.2


    # Ejercicio 5
    assert sueldoAPercibir(1000) == 800
    assert sueldoAPercibir(1200.0) == 960.0
    assert sueldoAPercibir(560) == 448
    assert sueldoAPercibir(978.5) == 782.8


    # Ejercicio 7
    assert signoNumero(8) == 'Es positivo'
    assert signoNumero(5.5) == 'Es positivo'
    assert signoNumero(0) == 'Es positivo'
    assert signoNumero(-5) == 'Es negativo'
    assert signoNumero(-12.8) == 'Es negativo'


    # Ejercicio 8
    assert relacionOrden(6, 7) == 'El primer número 6 es menor que el segundo 7'
    assert relacionOrden(10.5, 10.0) == 'El primer número 10.5 es mayor que el segundo 10.0'
    assert relacionOrden(37, 37) == 'Los dos números son iguales 37'
    assert relacionOrden(120.0, 120) == 'Los dos números son iguales 120.0'


    # Ejercicio 9
    assert suma(2, 4) == 'La suma de los dos números es: 6'
    assert suma(20, 35) == 'La suma de los dos números es: 55'
    assert suma(-8, 16) == 'No se calcula la suma porque alguno de los números o los dos no son positivos'
    assert suma(-47, -1) == 'No se calcula la suma porque alguno de los números o los dos no son positivos'


    # Ejercicio 10
    assert suma(2, 4) == 'La suma de los dos números es: 6'
    assert suma(-20, 35) == 'No se calcula la suma porque el primer número es negativo'
    assert suma(8, -16) == 'No se calcula la suma porque el segundo número es negativo'
    assert suma(-47, -1) == 'No se calcula la suma porque los dos números son negativos'


    # Ejercicio 11
    assert relacionSumaResultado(2, 3, 5) == 'Se cumple que 5 = 2 + 3'
    assert relacionSumaResultado(4, 12, 8) == 'Se cumple que 12 = 4 + 8'
    assert relacionSumaResultado(25, 11, 14) == 'Se cumple que 25 = 11 + 14'
    assert relacionSumaResultado(6, 2, 3) == 'Los números no se relacionan por suma y resultado'


    # Ejercicio 12
    assert sumaEnCondiciones(2, 3) == 'Almenos uno de los números no es par'
    assert sumaEnCondiciones(6, 12) == 'El primer número no es mayor que 50'
    assert sumaEnCondiciones(54, 90) == 'El segundo número no está entre 100 y 500'
    assert sumaEnCondiciones(60, 300) == 360


    # Ejercicio 13
    assert importeFinal(19) == 19
    assert importeFinal(50) == 47.5
    assert importeFinal(780) == 702.0
