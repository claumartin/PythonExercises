## 23. Leer por teclado dos números enteros positivos.
# Calcular la suma de los números pares e impares comprendidos entre los dos números leídos, ambos incluidos. 
# El programa tiene que funcionar independientemente de que el primero de los números tecleados sea mayor o menor que el segundo.

inicio = int(input('Introduzca el primer número entero positivo  '))
fin = int(input('Introduzca el segundo número entero positivo  '))

def sumaParesEnRango(inicio, fin):
    sumaPares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares
    else:
        for numero in range(fin, inicio + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares

def sumaImparesEnRango(inicio, fin):
    sumaImpares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares
    else:
        for numero in range(fin, inicio +1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares

def sumaParesImparesEnRango(inicio, fin):
    if inicio < 0 or fin < 0:
        return 'Se requieren dos números enteros positivos'
    else:
        return sumaParesEnRango(inicio, fin), sumaImparesEnRango(inicio, fin)

print(sumaParesImparesEnRango(inicio, fin))


## 24. Variante del programa anterior.
# Obligar al usuario a que los dos números introducidos sean positivos.
# Si el usuario introduce algún valor negativo, se visualiza un mensaje de aviso y se vuelve a pedir otro número.

def sumaParesEnRango(inicio, fin):
    sumaPares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares
    else:
        for numero in range(fin, inicio + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares

def sumaImparesEnRango(inicio, fin):
    sumaImpares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares
    else:
        for numero in range(fin, inicio +1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares

def sumaParesImparesEnRango(inicio, fin):
    return sumaParesEnRango(inicio, fin), sumaImparesEnRango(inicio, fin)

print('Se requieren dos números enteros positivos')
inicio = int(input('Introduzca el primer número  '))
fin = int(input('Introduzca el segundo número  '))

def calcularSumaParesImparesEnRango(inicio, fin):
    nuevoInicio = inicio
    nuevoFin = fin
    while nuevoInicio < 0 or nuevoFin < 0:
        if nuevoInicio < 0:
            nuevoInicio = int(input('El primer número no es entero positivo, introduzca uno correcto '))
        else:
            nuevoFin = int(input('El segundo número no es entero positivo, introduzca uno correcto'))
    assert nuevoInicio > 0 and nuevoFin > 0
    return sumaParesImparesEnRango(nuevoInicio, nuevoFin)

print(calcularSumaParesImparesEnRango(inicio, fin))


## 25. Variante ejercicio anterior.
# No permitir introducir dos números iguales.

def sumaParesEnRango(inicio, fin):
    sumaPares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares
    else:
        for numero in range(fin, inicio + 1):
            if numero % 2 == 0:
                sumaPares += numero
        return sumaPares
    
def sumaImparesEnRango(inicio, fin):
    sumaImpares = 0
    if inicio < fin:
        for numero in range(inicio, fin + 1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares
    else:
        for numero in range(fin, inicio +1):
            if numero % 2 != 0:
                sumaImpares += numero
        return sumaImpares

def sumaParesImparesEnRango(inicio, fin):
    return sumaParesEnRango(inicio, fin), sumaImparesEnRango(inicio, fin)

print('Se requieren dos números enteros positivos distintos')
inicio = int(input('Introduzca el primer número  '))
fin = int(input('Introduzca el segundo número  '))

def calcularSumaParesImparesEnRango(inicio, fin):
    nuevoInicio = inicio
    nuevoFin = fin
    while nuevoInicio < 0 or nuevoFin < 0:
        if nuevoInicio < 0:
            nuevoInicio = int(input('El primer número no es entero positivo, introduzca uno correcto '))
        else:
            nuevoFin = int(input('El segundo número no es entero positivo, introduzca uno correcto'))
    while nuevoInicio == nuevoFin:
        print('Los números proporcionados son iguales, introduzca dos números distintos')
        nuevoInicio = int(input('Introduzca el primer número  '))
        nuevoFin = int(input('Introduzca el segundo número  '))

    assert nuevoInicio > 0 and nuevoFin > 0
    assert nuevoInicio != nuevoFin

    return sumaParesImparesEnRango(nuevoInicio, nuevoFin)

print(calcularSumaParesImparesEnRango(inicio, fin))


# 26. Pedir por teclado un número entero positivo n, obligando al usuario a que sea positivo. 
# Siempre que se introduzca un número negativo, mostrar un mensaje de aviso.
# Pedir al usuario otro número y mantener este comportamiento hasta que el número que introduzca sea positivo. 

# A continuación ir calculando la suma siguiente:
# 1^2 + 2^2 + 3^2 + 4^2 + ...
# hasta que se satisfaga que dicha suma sea mayor que n.
 
# Mostrar la suma calculada y el último término que ha sido elevado al cuadrado y acumulado a la suma.

numero = int(input('Introduzca un número entero positivo  '))

def inputPositivo(numero):
    numeroActual = numero
    while numeroActual < 0:
        numeroActual = int(input('El valor proporcionado es negativo, introduzca un entero positivo  '))
    assert numeroActual >= 0
    return numeroActual

def sumaCuadradosEnRango(rango):
    ultimoTermino = 1
    suma = 0
    while suma <= rango:
        suma += (ultimoTermino ** 2)
        ultimoTermino += 1
    return(suma, ultimoTermino - 1)

print(sumaCuadradosEnRango(inputPositivo(numero)))


## 27. Pedir por teclado cuántas calificaciones tiene del alumno, a continuación las notas.
# Calcular y mostrar en consola la nota media.

numeroCalificaciones = int(input('Introduzca el número de calificaciones a registrar  '))

def sumaCalificaciones(numeroCalificaciones):
    index = 0
    suma = 0
    while index < numeroCalificaciones:
        suma += int(input('Introduzca nota: '))
        index += 1
    assert index == numeroCalificaciones
    return suma

def mediaCalificaciones(sumaCalificaciones, numeroCalificaciones):
    return sumaCalificaciones(numeroCalificaciones) / numeroCalificaciones

print(mediaCalificaciones(sumaCalificaciones, numeroCalificaciones))


## 28. Modifica el programa anterior para que no permita al usuario introducir notas mayores que 10. 
# a. El proceso de lectura finaliza cuando se introduzca una nota negativa. 
# b. El programa puede ser ejecutado varias veces.
#   Después de realizar el proceso para un alumno se visualiza el mensaje: ¿Desea calcular la media de otro alumno? Teclee S/N. 
# c. Si el usuario teclea S el programa vuelve a ejecutarse. Si teclea N finaliza su ejecución.

numeroCalificaciones = int(input('Introduzca el número de calificaciones a registrar  '))

def sumaCalificaciones(numeroCalificaciones):
    index = 0
    suma = 0
    while index < numeroCalificaciones:
        suma += int(input('Introduzca nota: '))
        index += 1
    assert index == numeroCalificaciones
    return suma

def mediaCalificaciones(sumaCalificaciones, numeroCalificaciones):
    return sumaCalificaciones(numeroCalificaciones) / numeroCalificaciones

print(mediaCalificaciones(sumaCalificaciones, numeroCalificaciones))

respuestaNuevaMedia = input('¿Desea calcular la media de otro alumno? Teclee S/N:  ')

def nuevaMedia(respuestaNuevaMedia):
    nuevaRespuesta = respuestaNuevaMedia
    while nuevaRespuesta == 'S':
        numeroCalificaciones = int(input('Introduzca el número de calificaciones a registrar  '))
        print(mediaCalificaciones(sumaCalificaciones, numeroCalificaciones))
        nuevaRespuesta = input('¿Desea calcular la media de otro alumno? Teclee S/N:  ')

nuevaMedia(respuestaNuevaMedia)
    



## CASOS TEST

if __name__ == '__main__':

    #Ejercicio 23
    assert sumaParesEnRango(1, 4) == 6
    assert sumaParesEnRango(2, 9) == 20
    assert sumaParesEnRango(4, 1) == 6
    assert sumaParesEnRango(9, 2) == 20

    assert sumaImparesEnRango(1, 4) == 4
    assert sumaImparesEnRango(2, 9) == 24
    assert sumaImparesEnRango(4, 1) == 4
    assert sumaImparesEnRango(9, 2) == 24

    assert sumaParesImparesEnRango(1, 4) == (6, 4)
    assert sumaParesImparesEnRango(9, 2) == (20, 24)
    assert sumaParesImparesEnRango(-5, 12) == 'Se requieren dos números enteros positivos'
    assert sumaParesImparesEnRango(5, -12) == 'Se requieren dos números enteros positivos'


    # Ejercicio 25
    assert sumaCuadradosEnRango(4) == (5, 2)
    assert sumaCuadradosEnRango(8) == (14, 3)
    assert sumaCuadradosEnRango(0) == (1, 1)
    assert sumaCuadradosEnRango(-8) == (0, 0)