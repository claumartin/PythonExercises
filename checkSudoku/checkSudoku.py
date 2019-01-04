from sudoku.checkCuadrado  import checkCuadrado
from sudoku.checkNumerosEnRango import checkNumerosEnRango
from sudoku.checkFilas import checkFilas
from sudoku.checkColumnas import checkColumnas

def checkSudoku(sudoku):

    assert isinstance(sudoku, list)
    
    if not checkCuadrado(sudoku) or not checkNumerosEnRango(sudoku) or not checkFilas(sudoku) or not checkColumnas:
        return False
    else:
        return True


if __name__ == '__main__':
    
    assert checkSudoku([[1,2,3],
                        [2,3,1],
                        [3,1,2]]) == True
                    
    assert checkSudoku([[1,2,3,4],
                        [2,3,1,3],
                        [3,1,2,3],
                        [4,4,4,2]]) == False

    assert checkSudoku([[1,2,3,4],
                        [2,3,1,2],
                        [4,1,2,3],
                        [2,3,1,4]]) == False
    
    assert checkSudoku([[1,2,3,4,5],
                        [2,3,1,5,6],
                        [4,5,2,1,3],
                        [3,4,5,2,1],
                        [5,6,4,3,2]]) == False

    assert checkSudoku([['a','b','c'],
                        ['b','c','a'],
                        ['c','a','b']]) == False
    
    assert checkSudoku([[1, 1.5],
                        [1.5, 1]]) == False
    
    assert checkSudoku([[1,2,3],
                        [2,3,1]]) == False
                    
    assert checkSudoku([[1,2,3],
                        [2,3,1],
                        [3,1]]) == False