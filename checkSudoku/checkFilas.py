def checkFilas(sudoku):
    for fila in sudoku:
        for element in fila:
            if fila.count(element) > 1:
                return False
    return True



if __name__ == '__main__':

    assert checkFilas([[1,2,3],
                      [2,3,1],
                      [3,1,2]]) == True

    assert checkFilas([[1,2,3,4],
                      [2,3,1,3],
                      [3,1,2,3],
                      [4,4,4,2]]) == False

    assert checkFilas([[1,2,3,4,5],
                      [2,3,1,5,6],
                      [4,5,2,1,3],
                      [3,4,5,2,1],
                      [5,6,4,3,2]]) == True

    assert checkFilas([[1, 1.5],
                      [1.5, 1]]) == True
    
    
    
