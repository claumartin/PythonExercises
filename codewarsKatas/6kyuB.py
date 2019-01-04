## Exclamation marks series #17: Put the exclamation marks and question marks to the balance, Are they balanced?
def balance(left, right):

    leftPoints = 0
    for sign in left:
        if sign == '!':
            leftPoints = leftPoints + 2
        elif sign == '?':
            leftPoints = leftPoints + 3
    
    rightPoints = 0
    for sign in right:
        if sign == '!':
            rightPoints = rightPoints + 2
        elif sign == '?':
            rightPoints = rightPoints + 3
    
    if leftPoints > rightPoints:
        return 'Left'
    elif leftPoints < rightPoints:
        return 'Right'
    else:
        return 'Balance'
       

## Round by 0.5 steps
def solution(number):
    
    integerNumber = int(number)
    decimals = number - integerNumber
    
    if decimals >= 0.75:
        return integerNumber + 1
    elif decimals >= 0.25 and decimals < 0.75:
        return integerNumber + 0.5
    else:
        return integerNumber




## CASOS TEST
if __name__ == '__main__':       

    assert balance("!!","??") == "Right"
    assert balance("!??","?!!") == "Left"
    assert balance("!?!!","?!?") == "Left"
    assert balance("!!???!????","??!!?!!!!!!!") == "Balance"


    assert round(4.2) == 4
    assert round(4.25) == 4
    assert round(4.4) == 4
    assert round(4.6) == 5
    assert round(4.75) == 5
    assert round(4.8) == 5
