## 6 KYU LEVEL KATAS (1/2)

# 1. Array.diff

'''
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from 
the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(given_array, item_to_remove):

    output_array = []
    for value in given_array:

        if value not in item_to_remove:
            output_array.append(value)

    return output_array


# 2. Are they the "same"?

'''
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) 
that checks whether the two arrays have the "same" elements, with the same 
multiplicities. "Same" means, here, that the elements in b are the elements 
in a squared, regardless of the order.

Examples:
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the 
square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square 
of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

Invalid arrays...

If we change the first number to something else, comp may not return true 
anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks...

a or b might be [] (all languages except R, Shell). a or b might be nil or null 
or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).

If a or b are nil (or null or None), the problem doesn't make sense so 
return false.

If a or b are empty then the result is self-evident.

a or b are empty or not empty lists.
'''

def areTheyTheSame(array1, array2):
    
    auxArray = array1
    if auxArray == None or array2 == None:
        return False
    
    for square in array2:
    
        position = 0
        
        while auxArray and position < len(array1):
        
            if auxArray[position] ** 2 == square:
                auxArray.remove(auxArray[position])
                position = 0
                break # return to loop over array2
                
            position += 1
            
            if position == len(auxArray):
                return False
                
    return True


# 3. Duplicate Encoder

'''
The goal of this exercise is to convert a string to a new string where each 
character in the new string is "(" if that character appears only once in the 
original string, or ")" if that character appears more than once in the original 
string. Ignore capitalization when determining if a character is a duplicate.

Examples:
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes

Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not 
the input!
'''

def duplicate_encode(word):

    string = word.casefold()
    newString = ''
    auxString= ''
    repeatedCharacters = ''

    for character in string:

            if character not in auxString:
                auxString = auxString + character
            else:
                repeatedCharacters = repeatedCharacters + character

    for position in string:

        if position not in repeatedCharacters:
            newString = newString + '('
        else:
            newString = newString + ')'

    return newString


# 4. Convert string to camel case

'''
Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized (known as Upper Camel Case, also often 
referred to as Pascal case).

Examples:
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''

def toCamelCase(text):

    result = ''
    for character in text:

        if character == '_' or character == '-':
            text = text.replace(character, ' ')

    if (' ') in text:   
            
        firstSpace = text.find(' ')
        firstWord = text[:firstSpace]
        titleString = text[firstSpace:]  
        titledString = titleString.title()
        newString = firstWord + titledString
        result = result + newString.replace(' ', '')
        
    return result


# 5. Loose Change

'''
Welcome young Jedi! In this Kata you must create a function that takes an amount 
of US currency in cents, and returns a dictionary/hash which shows the least 
amount of coins used to make up that amount. The only coin denominations 
considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and 
Quarters (25¢). Therefor the dictionary returned should contain exactly 4 
key/value pairs.

Notes:

If the function is passed either 0 or a negative number, the function should 
return the dictionary with all values equal to 0.
If a float is passed into the function, its value should be be rounded down, 
and the resulting dictionary should never contain fractions of a coin.

Examples:

loose_change(56)    ==>  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
loose_change(-435)  ==>  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
loose_change(4.935) ==>  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
'''

def loose_change(importe):

    caja = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0}
    resto = float(importe)
    while resto > 0:

        if resto >= 25:
            caja['Quarters'] = int(resto / 25)
            resto = resto % 25

        elif resto < 25 and resto >= 10:
            caja['Dimes'] = int(resto / 10)
            resto = resto % 10

        elif resto < 10 and resto >= 5:
            caja['Nickels'] = int(resto / 5)
            resto = resto % 5

        else:
            caja['Pennies'] = int(resto)
            resto = 0
    
    return caja


# 6. Dictionary Merge

'''
Your task is to implement a function that takes one or more dictionaries and 
combines them in one result dictionary.

The keys in the given dictionaries can overlap. In that case you should combine 
all source values in an array. Duplicate values should be preserved.

Here is an example:

source1 = {"A": 1, "B": 2} 
source2 = {"A": 3}

result = merge(source1, source2);
// result should have this content: {"A": [1, 3]}, "B": [2]}
You can assume that only valid dictionaries are passed to your function. The 
number of given dictionaries might be large. So take care about performance.
'''

def merge(*dicts):

    keysList = []
    for diccionario in dicts:

        for key in diccionario:

            keysList.append(key)

    merge = {}
    for key in keysList:

        merge[key] = []

        for diccionario in dicts:

            if key in diccionario:
                merge[key].append(diccionario[key])

    return merge


## TEST CASES
if __name__ == '__main__':

    # 1. Array.diff
    assert array_diff([1,2], [1]) == [2]
    assert array_diff([1,2,2], [1]) == [2,2]
    assert array_diff([1,2,2], [2]) == [1]
    assert array_diff([1,2,2], []) == [1,2,2]
    assert array_diff([], [1,2]) == []

    # 2. Are they the "same"?
    assert areTheyTheSame([121, 144, 19, 161, 19, 144, 19, 11], 
    [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]) == True
    
    assert areTheyTheSame([121, 144, 19, 161, 19, 144, 19, 11], 
    [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]) == False

    assert areTheyTheSame([121, 144, 19, 161, 19, 144, 19, 11], 
    [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]) == False
    
    assert areTheyTheSame([], []) == True

    assert areTheyTheSame([], None) == False

    assert areTheyTheSame([121, 144, 19, 161, 19, 144, 19, 11, 1008], 
    [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]) == False

    assert areTheyTheSame([10000000, 100000000], 
    [10000000 * 10000000, 100000000 * 100000000]) == True

    assert areTheyTheSame([10000001, 100000000], 
    [10000000 * 10000000, 100000000 * 100000000]) == False

    assert areTheyTheSame([2, 2, 3], [4, 9, 9]) == False

    # 3. Duplicate Encoder
    assert duplicate_encode("din") == "(((" 
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("

    # 4. Convert string to camel case
    assert toCamelCase('') == ''
    assert toCamelCase("the_stealth_warrior") == "theStealthWarrior"
    assert toCamelCase("The-Stealth-Warrior") == "TheStealthWarrior"
    assert toCamelCase("A-B-C") == "ABC"

    # 5. Loose change
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}

    # 6. Disctionary Merge
    assert merge({}, {}, {}) == {}
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}