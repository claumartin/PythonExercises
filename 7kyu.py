## 7 KYU LEVEL KATAS

# 1. Odd or Even?

'''
Given an array of numbers (a list in groovy), determine whether the sum of all 
of the numbers is odd or even.

Give your answer in string format as 'odd' or 'even'.

If the input array is empty consider it as: [0] (array with a zero).
'''

def oddOrEven(array):

    sum = 0
    for number in array:
        sum = sum + number

    if sum % 2 == 0:
        return 'even'
    else:
        return 'odd' 


# 2. Get the Middle Character

'''

'''

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


# 3. Predict your age!

'''
My grandfather always predicted how old people would get, and right before he 
passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example:

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86

Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation. 
Simply resubmit if that happens to you.
'''

def predict_age(*ages):

    result = 0
    for age in ages:

        i = age * age
        result = result + i

    result = result ** (1/2) /2
    return int(result)


# 4. The highest profit wins!

'''
Ben has a very simple idea to make some profit: she buys something and sells it 
again. Of course, this wouldn't give her any profit at all if she was simply to 
buy and sell it at the same price. Instead, she's going to buy it for the lowest 
possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given 
list/array.

Examples:

min_max([1,2,3,4,5])   == [1,5]
min_max([2334454,5])   == [5, 2334454]
min_max([1])           == [1, 1]
'''

def min_max(given_list):
    min_max = []
    min_max.append(min(given_list))
    min_max.append(max(given_list))
    return min_max


# 5. Make a function that does arithmetic!

'''
Given two numbers and an arithmetic operator (the name of it, as a string), 
return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number 
in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:

arithmetic(5, 2, "add")      => returns 7
arithmetic(5, 2, "subtract") => returns 3
arithmetic(5, 2, "multiply") => returns 10
arithmetic(5, 2, "divide")   => returns 2.5
ArithmeticFunction.arithmetic(5, 2, "add")      => returns 7
ArithmeticFunction.arithmetic(5, 2, "subtract") => returns 3
ArithmeticFunction.arithmetic(5, 2, "multiply") => returns 10
ArithmeticFunction.arithmetic(5, 2, "divide")   => returns 2

Try to do it without using if statements!
'''

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


# 6. You're a square!

'''
You like building blocks. You especially like building blocks that are squares. 
And what you even like more, is to arrange them into a square of square 
building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up 
with an ordinary rectangle! Those blasted things! If you just had a way to know, 
whether you're currently working in vain… Wait! That's it! You just have to 
check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the 
square of an integer; in other words, it is the product of some integer 
with itself.

The tests will always use some integral number, so don't worry about that in
dynamic typed languages.

Examples:

is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true  
isSquare(26) returns  false
'''

def is_square(input_number):

    if input_number < 0:
        return False

    elif input_number ** (1/2) == int(input_number ** (1/2)):
        return True

    else:
        return False


# 7. List Filtering

'''
In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.

Examples:

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
''' 

def is_integer(int_input):

    if isinstance(int_input, int):
          return True
    return False
    
def filter_list(given_list):

    filtered_list = []
    for element in given_list:

        if is_integer(element) and element not in filtered_list:
            filtered_list.append(element)

    return filtered_list  


# 8. Number of People in the Bus

'''
There is a bus moving in the city, and it takes and drop some people in 
each bus stop.

You are provided with a list (or array) of integer arrays (or tuples). 
Each integer array has two items which represent number of people get into bus 
(The first item) and number of people get off the bus (The second item) in 
a bus stop.

Your task is to return number of people who are still in the bus after the last 
bus station (after the last array). Even though it is the last bus stop, the bus 
is not empty and some people are still in the bus, and they are probably 
sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the 
bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the 
first bus stop.
'''

def number(bus_stops):
    people = 0
    for tuple in bus_stops:
        people = people + tuple[0] - tuple[1]
    return people


# 9. Complementary DNA

'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and 
carries the "instructions" for the development and functioning of living 
organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and 
"G". You have function with one side of the DNA (string, except for Haskell); 
you need to get the other complementary side. DNA strand is never empty or there 
is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ 
(source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
'''

def dna_strand(dna):

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


# 10. Leap Years

'''
In this kata you should simply determine, whether a given year is a leap year 
or not. In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years
Additional Notes:

Only valid years (positive integers) will be tested, so you don't have to 
validate them
Examples can be found in the test fixture.
'''

def isLeapYear(year):

    if year >= 0:
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False


## TEST CASES
if __name__ == '__main__':

    # 1. Odd or even?
    assert oddOrEven([0, 1, 2]) == 'odd'
    assert oddOrEven([0, 1, 3]) == 'even'
    assert oddOrEven([1023, 1, 2]) == 'even'     


    assert get_middle("test") == "es"
    assert get_middle("testing") == "t"
    assert get_middle("middle") == "dd"
    assert get_middle("A") == "A"
    assert get_middle("of") == "of"
    
    # 3. Predict your age!
    assert predict_age(65,60,75,55,60,63,64,45) == 86

    # 4. The highest profit wins!
    assert min_max([1,2,3,4,5]) == [1,5]
    assert min_max([2334454,5]) == [5, 2334454]
    assert min_max([1]) == [1, 1]

    # 5. Make a function that does arithmetic!
    assert arithmetic(5, 2, "add") == 7
    assert arithmetic(5, 2, "subtract") == 3
    assert arithmetic(5, 2, "multiply") == 10
    assert arithmetic(5, 2, "divide") == 2.5

    # 6. You're a square!
    assert is_square(-1) == False
    assert is_square(0) == True
    assert is_square(3) == False
    assert is_square(4) == True
    assert is_square(25) == True  
    assert is_square(26) == False

    # 7. List filtering
    assert filter_list([1,2,'a','b']) == [1,2]
    assert filter_list([1,'a','b',0,15]) == [1,0,15]
    assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

    # 8. Number of People in the Bus
    assert number([[10,0],[3,5],[5,8]]) == 5
    assert number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) == 17
    assert number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) == 21

    # 9. Complementary DNA
    assert dna_strand("AAAA") == "TTTT"
    assert dna_strand("ATTGC") == "TAACG"
    assert dna_strand("GTAT") == "CATA"

    # 10. Leap years
    assert isLeapYear(1984) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(1234) == False
    assert isLeapYear(1100) == False
    assert isLeapYear(0000) == True