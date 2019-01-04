## Array.diff
def array_diff(array, toRemove):
    newArray = []
    for value in array:
        if value not in toRemove:
            newArray.append(value)
    return newArray


## Are they the "same"?
def areTheyTheSame(array1, array2):
    arraySupport = array1
    if arraySupport == None or array2 == None:
        return False
    
    for square in array2:
    
        position = 0
        
        while arraySupport and position < len(array1):
        
            if arraySupport[position] ** 2 == square:
                arraySupport.remove(arraySupport[position])
                position = 0
                break # return to loop over array2
                
            position += 1
            
            if position == len(arraySupport):
                return False
                
    return True


## Duplicate Encoder
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


## Convert string to camel case
def to_camel_case(text):
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


## Loose Change
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


## Dictionary Merge
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




## CASOS TEST
if __name__ == '__main__':

    assert array_diff([1,2], [1]) == [2]
    assert array_diff([1,2,2], [1]) == [2,2]
    assert array_diff([1,2,2], [2]) == [1]
    assert array_diff([1,2,2], []) == [1,2,2]
    assert array_diff([], [1,2]) == []


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


    assert duplicate_encode("din") == "(((" 
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("


    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"


    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}


    assert merge({}, {}, {}) == {}
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}