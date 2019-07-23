## 6 KYU LEVEL KATAS (2/2)

# 7. Exclamation marks series

'''
Each exclamation mark weight is 2; Each question mark weight is 3. Put two 
string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, 
return "Right"; If they are balanced, return "Balance".

Examples:

balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
'''

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
       

# 8. Round by 0.5 steps

'''
Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5

Round up if number is as close to previous and next 0.5 steps.
'''

def round_it(given_number):
    
    to_int_given_number = int(given_number)
    decimals = given_number - to_int_given_number
    
    if decimals >= 0.75:
        return to_int_given_number + 1

    elif decimals > 0.25 and decimals < 0.75:
        return to_int_given_number + 0.5
    else:
        return to_int_given_number


# 9. CamelCase Method

'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or 
camelCase in Java) for strings. All words must have their first letter 
capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
'''

def toCamelCase(capitalizedString):
    
    capitalizedString = capitalizedString.capitalize()
    toCamelcaseString = ''

    for index, char in enumerate(capitalizedString):


        if capitalizedString[index - 1] == ' ':
        
            uppercasedChar = char.title()
            toCamelcaseString = toCamelcaseString + uppercasedChar

        else:

            toCamelcaseString = toCamelcaseString + char
        
    camelcasedString = toCamelcaseString.replace(' ', '')

    return camelcasedString


## TEST CASES
if __name__ == '__main__':       

    # 7. Exclamation marks series
    assert balance("!!","??") == "Right"
    assert balance("!??","?!!") == "Left"
    assert balance("!?!!","?!?") == "Left"
    assert balance("!!???!????","??!!?!!!!!!!") == "Balance"

    # 8. Round by 0.5 steps
    assert round_it(4.2) == 4
    assert round_it(4.25) == 4
    assert round_it(4.4) == 4.5
    assert round_it(4.6) == 4.5
    assert round_it(4.75) == 5
    assert round_it(4.8) == 5

    # 9. CamelCase Method
    assert toCamelCase("test case") == "TestCase"
    assert toCamelCase("camel case method") == "CamelCaseMethod"
    assert toCamelCase("say hello ") == "SayHello"
    assert toCamelCase(" camel case word") == "CamelCaseWord"
    assert toCamelCase("") == ""  