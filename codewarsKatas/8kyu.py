## Remove First and Last Character
def remove_char(s):
    return (s[1:-1])
    
s='string'
print (remove_char(s))


## The Feast of Many Beasts
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False
    pass

beast= "great blue heron"
dish= "garlic naan"
print(feast(beast, dish))


## Transportation on vacation
def rental_car_cost(d):
    price= d * 40
    if d < 3:
        return price
    elif d >= 3 and d < 7:
        return price - 20
    else:
        return price - 50
        
d= 7
print(rental_car_cost(d))


## Convert a Number to a String!
def number_to_string(num):
    string= str(num)
    return string


## String repeat
def repeat_str(repeat, string):
    return string * repeat


## Reversed sequence
def reverse_seq(n):
    sequence = [n]
    index = n
    while index > 1:
        index = index - 1
        sequence.append(index)
    return sequence


## Rock Paper Scissors!
def rps(p1, p2):
    if p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    else:
        return "Player 2 won!"


## Double Char
def double_char(s):
    newString = ""
    for letter in s:
        double = letter * 2
        newString = newString + double
    return newString


## Remove exclamation marks
def remove_exclamation_marks(s):
    newString = s.replace("!", "")
    return newString


## Square(n) Sum
def square_sum(list):
    result = 0
    for number in list:
        square= number ** 2
        result = result + square
    return result


## Is he gonna survive?
def hero(bullets, dragons):
    bulletsNeeded= dragons * 2
    if bullets >= bulletsNeeded:
        return True
    else:
        return False


## Even or Odd
def even_or_odd(number):
    myNumber= int(number)
    if 0 == myNumber % 2:
        return 'Even'
    else:
        return 'Odd'


## Volume of a Cuboid
def getVolumeOfCubiod(length, width, height):
    return float(length * width * height)




## CASOS TEST
if __name__ == '__main__':

    assert remove_char('eloquent') == 'loquen'
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''


    assert feast("great blue heron", "garlic naan") == True
    assert feast("chickadee", "chocolate cake") == True
    assert feast("brown bear", "bear claw") == False


    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270


    assert number_to_string(67) == '67'


    assert repeat_str(4, 'a') ==  'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'


    assert reverse_seq(5) == [5,4,3,2,1]
    assert reverse_seq(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'paper') == "Player 1 won!"
    assert rps('paper', 'rock') == "Player 1 won!"

    assert rps('scissors', 'rock')  =="Player 2 won!"
    assert rps('paper', 'scissors') == "Player 2 won!"
    assert rps('rock', 'paper') == "Player 2 won!"

    assert rps('rock', 'rock') == 'Draw!'
    assert rps('scissors', 'scissors') == 'Draw!'
    assert rps('paper', 'paper') == 'Draw!'


    assert double_char("String") =="SSttrriinngg"
    assert double_char("Hello World") =="HHeelllloo  WWoorrlldd"
    assert double_char("1234!_ ") =="11223344!!__  "


    assert remove_exclamation_marks("Hello World!") == "Hello World"
    assert remove_exclamation_marks("Hello World!!!") == "Hello World"
    assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
    assert remove_exclamation_marks("") == ""
    assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"


    assert square_sum([1,2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50


    assert hero(10, 5) == True
    assert hero(7, 4) == False
    assert hero(4, 5) == False
    assert hero(100, 40) == True
    assert hero(1500, 751) == False
    assert hero(0, 1) == False


    assert even_or_odd(2) == "Even"
    assert even_or_odd(0) == "Even"
    assert even_or_odd(7) == "Odd"
    assert even_or_odd(1) == "Odd"
    assert even_or_odd(-1) == "Odd"


    assert getVolumeOfCubiod(1, 2, 2) == 4
    assert getVolumeOfCubiod(6.3, 2, 5) == 63