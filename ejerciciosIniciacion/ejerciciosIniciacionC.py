## 15. Escribir cinco veces el mensaje 'Estamos estudiando metodología de la programación'.

miMensaje = 'Estamos estudiando metodología de la programación'

def escribeCincoVeces(mensaje):
    index = 0
    while index < 5:
        print(mensaje)
        index += 1
    return mensaje

escribeCincoVeces(miMensaje)


## 16.  Mostrar por pantalla los 30 primeros números naturales (del 1 al 30), así como su media aritmética.

def mostrarNumerosNaturalesEnRango(inicio, fin):
    for numero in range(inicio, fin + 1):
        print(numero)

mostrarNumerosNaturalesEnRango(1, 30)

def mediaAritmetica(inicio, fin):
    total = 0
    for numero in range(inicio, fin + 1):
        total += numero
    return total / fin

print(mediaAritmetica(1, 30))


## 17. Calcular y mostrar por pantalla la suma de los números comprendidos entre dos número introducidos por teclado.
#La suma de los pares por un lado y la suma de los impares por otro.

inicio =int(input('Introduzca el número de inicio del sumatorio  '))
fin = int(input('Introduzca el número final del sumatorio  '))

def sumaParesImparesEnRango(inicio, fin):
    pares = 0
    impares = 0
    for numero in range(inicio, fin +1):
        if numero % 2 == 0:
            pares += numero
        else:
            impares += numero
    return pares, impares

print(sumaParesImparesEnRango(inicio, fin))


## 18. Mostrar los n-primeros múltiplos de 2, siendo n un valor leído por teclado.

def numerosParEnRango(limite):
    pares = []
    index = 0
    while len(pares) < limite:
        if index % 2 == 0:
            pares.append(index)
        index += 1
    return pares

limite = float(input('Introduzca la cantidad de números pares a mostrar '))
print(numerosParEnRango(limite))


## 19. Leer por teclado 5 números enteros positivos.
# Escribir cuál es el mayor de los números introducidos.  	

datosIntroducidos = input('Introduzca los 5 números enteros a comparar, separados por comas  ')

def conversionToFloatList(string):
    string = string.split(',')
    numerosIntroducidos = []
    for index, numero in enumerate(string):
        numerosIntroducidos.append(float(numero))
    return numerosIntroducidos   

def calcularMayor(numeros):
    mayor = numeros[0]
    for index, numero in enumerate(numeros):
        if numero > mayor:
            mayor = numero
    return mayor

def mostrarResultado(datosIntroducidos):
    if len(conversionToFloatList(datosIntroducidos)) != 5:
        return 'No has introducido 5 números enteros'
    else:
        return calcularMayor(conversionToFloatList(datosIntroducidos))

print(mostrarResultado(datosIntroducidos))


## 20. Variante ejercicio anterior.
# Chequear que el usuario no introduzca números negativos. 
# Si se da esta circunstancia mostrar un mensaje de error, forzando al usuario a que introduzca números positivos.

datosIntroducidos = input('Introduzca los 5 números enteros positivos a comparar, separados por comas  ')

def conversionToFloatList(string):
    string = string.split(',')
    numerosIntroducidos = []
    for index, numero in enumerate(string):
        numerosIntroducidos.append(float(numero))
    return numerosIntroducidos   

def calcularMayor(numeros):
    mayor = numeros[0]
    for index, numero in enumerate(numeros):
        if numero < 0:
            return None
    return max(numeros)

def mostrarResultado(datosIntroducidos):
    if len(conversionToFloatList(datosIntroducidos)) != 5:
        return 'No has introducido 5 números enteros'
    elif calcularMayor(conversionToFloatList(datosIntroducidos)) == None:
        return 'Almenos un número de los introducidos es negativo'
    else:
        return calcularMayor(conversionToFloatList(datosIntroducidos))

print(mostrarResultado(datosIntroducidos))


## 21. Pedir por teclado 5 números positivos, forzando al usuario a que únicamente introduzca valores positivos. 
# Mostrar el valor más pequeño y cuál es el mayor de los introducidos por el usuario.

datosIntroducidos = input('Introduzca los 5 números enteros positivos a comparar, separados por comas  ')

def conversionToFloatList(string):
    string = string.split(',')
    numerosIntroducidos = []
    for index, numero in enumerate(string):
        numerosIntroducidos.append(float(numero))
    return numerosIntroducidos   

def calcularMayor(numeros):
    mayor = numeros[0]
    for index, numero in enumerate(numeros):
        if numero < 0:
            return None
    return max(numeros)

def calcularMenor(numeros):
    for numero in numeros:
        if numero < 0:
            return None
    return min(numeros)

def mostrarResultado(datosIntroducidos):
    if len(conversionToFloatList(datosIntroducidos)) != 5:
        return 'No has introducido 5 números enteros'
    elif calcularMayor(conversionToFloatList(datosIntroducidos)) == None:
        return 'Almenos un número de los introducidos es negativo'
    else:
        return calcularMayor(conversionToFloatList(datosIntroducidos)), calcularMenor(conversionToFloatList(datosIntroducidos))

print(mostrarResultado(datosIntroducidos))


## 22. Variante ejercicio anterior.
# El usuario ha de indicar antes cuántos números van a ser leídos, 
# mostrar el mensaje: 'Introduzca cuántos números tienen que leerse por teclado: _'

cuantosComparar = input('Introduzca cuántos números han de leerse por teclado  ')
datosIntroducidos = input('Introduzca los 5 números enteros positivos a comparar, separados por comas  ')

def conversionToFloatList(string):
    string = string.split(',')
    numerosIntroducidos = []
    for numero in string:
        if len(numerosIntroducidos) < float(cuantosComparar):
            numerosIntroducidos.append(float(numero))
    return numerosIntroducidos   

def calcularMayor(numeros):
    mayor = numeros[0]
    for index, numero in enumerate(numeros):
        if numero < 0:
            return None
    return max(numeros)

def calcularMenor(numeros):
    for numero in numeros:
        if numero < 0:
            return None
    return min(numeros)

def mostrarResultado(datosIntroducidos):
    if calcularMayor(conversionToFloatList(datosIntroducidos)) == None:
        return 'Almenos un número de los introducidos es negativo'
    else:
        return calcularMayor(conversionToFloatList(datosIntroducidos)), calcularMenor(conversionToFloatList(datosIntroducidos))

print(mostrarResultado(datosIntroducidos))




##CASOS TEST

if __name__ == '__main__':
    
    # Ejercicio 16
    assert mediaAritmetica(1, 30) == 15.5


    # Ejercicio 17
    assert sumaParesImparesEnRango(1,4) == (6, 4)
    assert sumaParesImparesEnRango(2, 6) == (12, 8)
    assert sumaParesImparesEnRango(-36, 1) == (-342, -323)
    assert sumaParesImparesEnRango(24, 56) == (680, 640)


    # Ejercicio 18
    assert numerosParEnRango(10) == [0, 2, 4, 6, 8, 10, 12, 
    14, 16, 18]
    assert numerosParEnRango(25) == [0, 2, 4, 6, 8, 10, 
    12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 
    40, 42, 44, 46, 48]
    assert numerosParEnRango(82) == [0, 2, 4, 6, 8, 10, 
    12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 
    38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 
    64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 
    90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 
    114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 
    136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 
    158, 160, 162]


    # Ejercicio 19
    assert conversionToFloatList('1, 2, 3, 4, 5') == [1, 2, 3, 4, 5]
    assert conversionToFloatList('4, 5, 6, 2, 7') ==[4, 5, 6, 2, 7]
    assert conversionToFloatList('12, 4, 3, 3, 5') == [12, 4, 3, 3, 5]
    assert conversionToFloatList('5, 4, -10, 9, 1') == [5, 4, -10, 9, 1]

    assert calcularMayor([1, 2, 3, 4, 5]) == 5
    assert calcularMayor([4, 5, 6, 2, 7]) == 7
    assert calcularMayor([12, 4, 3, 3, 9]) == 12
    assert calcularMayor([5, 4, -10, 9, 1]) == 9

    assert calcularMayor(conversionToFloatList('1, 2, 3, 4, 5')) == 5
    assert calcularMayor(conversionToFloatList('4, 5, 6, 2, 7')) == 7
    assert calcularMayor(conversionToFloatList('12, 4, 3, 3, 9')) == 12
    assert calcularMayor(conversionToFloatList('5, 4, -10, 9, 1')) == 9
    
    assert mostrarResultado('1, 2, 3, 4, 5') == 5
    assert mostrarResultado('1, 2, 3, 4, 5, 6, 7, 8, 9, 10') == 'No has introducido 5 números enteros'


    # Ejercicio 20
    assert calcularMayor(conversionToFloatList('1, 2, 3, 4, 5')) == 5
    assert calcularMayor(conversionToFloatList('4, 5, 6, 2, 7')) == 7
    assert calcularMayor(conversionToFloatList('12, 4, 3, 3, 9')) == 12
    assert calcularMayor(conversionToFloatList('5, 4, -10, 9, 1')) == None
    
    assert mostrarResultado('1, 2, 3, 4, 5') == 5
    assert mostrarResultado('1, 2, 3, 4, 5, 6, 7, 8, 9, 10') == 'No has introducido 5 números enteros'
    assert mostrarResultado('32, 15, -20, -4, 9') == 'Almenos un número de los introducidos es negativo'


    # Ejercicio 21
    assert calcularMenor(conversionToFloatList('1, 2, 3, 4, 5')) == 1
    assert calcularMenor(conversionToFloatList('4, 5, 6, 2, 7')) == 2
    assert calcularMenor(conversionToFloatList('12, 4, 3, 3, 9')) == 3
    assert calcularMenor(conversionToFloatList('5, 4, -10, 9, 1')) == None
    
    assert mostrarResultado('1, 2, 3, 4, 5') == (5, 1)
    assert mostrarResultado('1, 2, 3, 4, 5, 6, 7, 8, 9, 10') == 'No has introducido 5 números enteros'
    assert mostrarResultado('32, 15, -20, -4, 9') == 'Almenos un número de los introducidos es negativo'


    # Ejercicio 22
    if cuantosComparar == 5:
        assert mostrarResultado('1, 2, 3, 4, 5') == (5, 1)
        assert mostrarResultado('1, 2, 3, 4, 5, 6, 7, 8, 9, 10') == (5, 1)
        assert mostrarResultado('32, 15, -20, -4, 9') == 'Almenos un número de los introducidos es negativo'

    if cuantosComparar == 3:
        assert mostrarResultado('3, 4, 1, -3, 8') == (4, 1)

    if cuantosComparar == 8:
        assert mostrarResultado('3, 4, 5, 2, 70, 46, 18, 25, 111, 32, 1') == (70, 2)
