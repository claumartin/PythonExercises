def checkNumerosEnRango(sudoku):
    for fila in sudoku:
        for elemento in fila:
            if not isinstance(elemento, int):
                return False
            elif elemento > len(sudoku):
                return False
    return True


if __name__ == '__main__':

    assert checkNumerosEnRango([[1,2,3],
                                [2,3,1],
                                [3,1,2]]) == True
    
    assert checkNumerosEnRango([[1,2,3,4,5],
                               [2,3,1,5,6],
                               [4,5,2,1,3],
                               [3,4,5,2,1],
                               [5,6,4,3,2]]) == False

    assert checkNumerosEnRango([[1, 1.5],
                               [1.5, 1]]) == False

    assert checkNumerosEnRango([['a','b','c'],
                                ['b','c','a'],
                                ['c','a','b']]) == False
                                            