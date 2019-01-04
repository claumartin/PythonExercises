## Odd or Even?
def oddOrEven(arr):
    sum = 0
    for number in arr:
        sum = sum + number
    modulus= sum % 2
    if modulus == 0:
        return 'even'
    else:
        return 'odd'


## Get the Middle Character
def get_middle(s):
    length = len(s)
    if length % 2 != 0:
        return s[int(length / 2)]
    else:
        leftString = s[ : int(length / 2)]
        leftMiddle = leftString[-1]
        rightString = s[int(length / 2):]
        rightMiddle = rightString[0]
        return leftMiddle + rightMiddle


## Predict your age!
def predict_age(*ages):
    result = 0
    for age in ages:
        i = age * age
        result = result + i
    result = result ** (1/2) /2
    return int(result)


## The highest profit wins!
def min_max(lst):
    newLst = []
    newLst.append(min(lst))
    newLst.append(max(lst))
    return newLst


## Make a function that does arithmetic!
def arithmetic(a, b, operator):
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b
    else:
        return 'Values not admitted'


## You're a square!
def is_square(inp):
    if inp < 0:
        return False
    elif inp ** (1/2) == int(inp ** (1/2)):
        return True
    else:
        return False


## List Filtering
def is_integer(n):
    if isinstance(n, int):
          return True
    return False
    
def filter_list(l):
    l2 = []
    for element in l:
        if is_integer(element) and element not in l2:
            l2.append(element)
        else:             
            pass
    return l2  


## Number of People in the Bus
def number(bus_stops):
    stillPeople = 0
    for tuple in bus_stops:
        stillPeople = stillPeople + tuple[0] - tuple[1]
    return stillPeople


## Complementary DNA
def DNA_strand(dna):
    equals = ''
    for i in dna:
        if i == 'C':
            equals = equals + 'G'
        elif i == 'G':
            equals = equals + 'C'
        elif i == 'A':
            equals = equals + 'T'
        elif i == 'T':
            equals = equals + 'A'
    return equals


## Leap Years
def isLeapYear(year):
    if year >= 0:
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False




## CASOS TEST
if __name__ == '__main__':

    assert oddOrEven([0, 1, 2]) == 'odd'
    assert oddOrEven([0, 1, 3]) == 'even'
    assert oddOrEven([1023, 1, 2]) == 'even'     


    assert get_middle("test") =="es"
    assert get_middle("testing") =="t"
    assert get_middle("middle") =="dd"
    assert get_middle("A") =="A"
    assert get_middle("of") =="of"


    assert predict_age(65,60,75,55,60,63,64,45) == 86


    assert min_max([1,2,3,4,5]) == [1,5]
    assert min_max([2334454,5]) == [5, 2334454]
    assert min_max([1]) == [1, 1]


    assert arithmetic(5, 2, "add")      == 7
    assert arithmetic(5, 2, "subtract") == 3
    assert arithmetic(5, 2, "multiply") == 10
    assert arithmetic(5, 2, "divide")   == 2.5


    assert is_square(-1) ==  False
    assert is_square(0) ==   True
    assert is_square(3) ==   False
    assert is_square(4) ==   True
    assert is_square(25) ==  True  
    assert is_square(26) ==  False


    assert filter_list([1,2,'a','b']) == [1,2]
    assert filter_list([1,'a','b',0,15]) == [1,0,15]
    assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


    assert number([[10,0],[3,5],[5,8]]) == 5
    assert number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) == 17
    assert number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) == 21


    assert DNA_strand("AAAA") == "TTTT"
    assert DNA_strand("ATTGC") == "TAACG"
    assert DNA_strand("GTAT") == "CATA"


    assert isLeapYear(1984) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(1234) == False
    assert isLeapYear(1100) == False
    assert isLeapYear(0000) == True