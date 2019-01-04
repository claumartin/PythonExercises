
def insertionSort(array):

    for position in range(1, len(array)):

        index = position
        element = array[position]
        
        while (index > 0) and (element < array[index - 1]):
            array[index] = array[index - 1]
            index -= 1

        array[index] = element

    return array


### CASOS TEST

if __name__ == '__main__':

    ## 1. Caso simple enteros

    arrayA = [1, 3, 2]
    assert insertionSort(arrayA) == sorted(arrayA)

    ## 2. Caso simple strings

    arrayB = ['a', 'u', 'i', 'e', 'o']
    assert insertionSort(arrayB) == sorted(arrayB)

    ## 3. Caso números reales

    arrayC = [1.4, 5, 3, 3.5, 2, 4.1]
    assert insertionSort(arrayC) == sorted(arrayC)

    ## 4. Caso strings con mayúsculas
    # Ordena primero mayúsculas, después minúsculas
    arrayD = ['a', 'b', 'A', 'd', 'c', 'P']
    assert insertionSort(arrayD) == sorted(arrayD)

    ## 5. Caso con cadenas de caracteres

    arrayE = ['spam', 'ham', 'elmo']
    assert insertionSort(arrayE) == sorted(arrayE)
	

    ## 6. Casos random

    from random import shuffle

    def createRandomList(length):

        array = [element for element in range(length)]
        shuffle(array)

        assert len(array) == length
        return array

    # Para listas de 10 elementos
    myList = createRandomList(10)
    assert insertionSort(myList) == sorted(myList)


    # Para listas de 25 elementos

    myList = createRandomList(25)
    assert insertionSort(myList) == sorted(myList)

    # Para listas de 100 elementos...
    # Este programa no soporta listas de más de 25 elementos



