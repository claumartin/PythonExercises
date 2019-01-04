def checkCuadrado(sudoku):
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True



if __name__ == '__main__':
    
    assert checkCuadrado([[1,2,3,4],
                         [2,3,1,3],
                         [3,1,2,3],
                         [4,4,4,2]]) == True
    
    assert checkCuadrado([['a','b','c'],
                         ['b','c','a'],
                         ['c','a','b']]) == True

    assert checkCuadrado([[1,2,3],
                         [2,3,1],
                         [3,1]]) == False

    assert checkCuadrado([[1, 1.5],
                         [1.5, 1]]) == True

    assert checkCuadrado([[1,2,3],
                         [2,3,1]]) == False

    assert checkCuadrado([[1,2,3],
                        [2,3,1],
                        [3,1]]) == False
            
                                    
