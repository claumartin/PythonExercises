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
                





if __name__ == '__main__':

    assert toCamelCase("test case") == "TestCase"
    assert toCamelCase("camel case method") == "CamelCaseMethod"
    assert toCamelCase("say hello ") == "SayHello"
    assert toCamelCase(" camel case word") == "CamelCaseWord"
    assert toCamelCase("") == ""    