def checkColumnas(sudoku):
    
    primeraFila = sudoku[0]

    for elemento in primeraFila:

        posicionPrimeraFila = 0
        ultimaFila = len(sudoku) - 1
        posicionFilaActual = 1

        while posicionFilaActual <= ultimaFila:

            filaActual = sudoku[posicionFilaActual]

            if filaActual.index(elemento) == primeraFila.index(elemento):
                return False
            else:
                print(filaActual.index(elemento), primeraFila.index(elemento))
                posicionFilaActual += 1
                
    return True
    


if __name__ == '__main__':

    assert checkColumnas([[1,2,3],
                         [2,3,1],
                         [3,1,2]]) == True

    assert checkColumnas([[1,2,3,4],
                         [2,4,1,3],
                         [3,1,2,4],
                         [1,4,3,2]]) == False
    
    assert checkColumnas([[1, 2, 3, 4, 5, 6],
                         [2, 3, 4, 5, 6, 1],
                         [3, 4, 5, 6, 1, 2],
                         [4, 5, 6, 1, 2, 3],
                         [5, 6, 1, 2, 3, 4],
                         [6, 1, 2, 3, 4, 5]]) == True
    
    assert checkColumnas([[1, 2, 3, 4],
                         [2, 3, 4, 1],
                         [1, 2, 3, 4],
                         [4, 1, 2, 3]]) == False
                        