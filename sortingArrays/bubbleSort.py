def bubbleSort(array):

    lenghtArray = len(array)
    changes = True
    position = 0

    while (changes == True):
        
        changes = False
        for position in range(lenghtArray - 1):
                
                if array[position] > array[position + 1]:
                    array[position], array[position + 1] = array[position + 1], array[position]
                    #intercambio de elementos
                    changes = True

    return array            




###CASOS TEST

if __name__ == '__main__':

    ## 1. Caso simple enteros

    arrayA = [1, 3, 2]
    assert bubbleSort(arrayA) == sorted(arrayA)

    ## 2. Caso simple strings

    arrayB = ['a', 'u', 'i', 'e', 'o']
    assert bubbleSort(arrayB) == sorted(arrayB)

    ## 3. Caso números reales

    arrayC = [1.4, 5, 3, 3.5, 2, 4.1]
    assert bubbleSort(arrayC) == sorted(arrayC)

    ## 4. Caso strings con mayúsculas
    # Ordena primero mayúsculas, después minúsculas
    arrayD = ['a', 'b', 'A', 'd', 'c', 'P']
    assert bubbleSort(arrayD) == sorted(arrayD)

    ## 5. Caso con cadenas de caracteres

    arrayE = ['spam', 'ham', 'elmo']
    assert bubbleSort(arrayE) == sorted(arrayE)
	

    ## 6. Casos random

    from random import shuffle

    def createRandomList(length):

        array = [element for element in range(length)]
        shuffle(array)

        assert len(array) == length
        return array

    # Para listas de 15 elementos

    myList = createRandomList(15)
    assert bubbleSort(myList) == sorted(myList)

    # Para listas de 100 elementos...
    # Este programa no soporta listas a partir de los 20 elementos