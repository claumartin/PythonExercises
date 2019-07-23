## 8 KYU LEVEL KATAS

# 1. Remove First and Last Character

'''
It's pretty straightforward. 
The goal is to create a function that removes the first and last characters 
of a string. 
It's given one parameter, the original string. 
Don't have to worry with strings with less than two characters.
'''

def remove_char(s):
    return (s[1:-1])


# 2. The Feast of Many Beasts

'''
All of the animals are having a feast! Each animal is bringing one dish. 
There is just one rule: the dish must start and end with the same letters as 
the animal's name. For example, the great blue heron is bringing garlic naan 
and the chickadee is bringing chocolate cake.

Write a function feast that takes the animal's name and dish as arguments and 
returns true or false to indicate whether the beast is allowed to bring the 
dish to the feast.

Assume that beast and dish are always lowercase strings, and that each has at 
least two letters. Beast and dish may contain hyphens and spaces, but these 
will not appear at the beginning or end of the string. They will not contain 
numerals.
'''

def feast(beast, dish):

    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False


# 3. Transportation on vacation

'''
After a hard quarter in the office you decide to get some rest on a vacation. So
you will book a flight for you and your girlfriend and try to leave all the
mess behind you.

You will need a rental car in order for you to get around in your vacation. 
The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, 
you get $50 off your total. Alternatively, if you rent the car for 3 or more 
days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''

def rental_car_cost(d):

    price = d * 40

    if d < 3:
        return price
    elif d >= 3 and d < 7:
        return price - 20
    else:
        return price - 50
        

# 4. String repeat

'''
Write a function called repeatStr which repeats the given string string exactly 
n times.

Examples:
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'''

def repeatStr(repeat, string):
    return string * repeat


# 5. Rock Paper Scissors!

'''
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rock_paper_scirrors('scissors','paper') // Player 1 won!
rock_paper_scirrors('scissors','rock') // Player 2 won!
rock_paper_scirrors('paper','paper') // Draw!
'''

def rock_paper_scirrors(p1, p2):
    
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


# 6. Double Char

'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples:

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
'''

def double_char(s):

    new_string = ""
    for letter in s:

        double = letter * 2
        new_string = new_string + double
    
    return new_string


# 7. Remove explamation marks

'''
Write function RemoveExclamationMarks which removes all exclamation marks from a
given string.
'''

def remove_exclamation_marks(s):
    new_string = s.replace("!", "")
    return new_string


# 8. Square(n) sum

'''
Complete the square sum function so that it squares each number passed into it 
and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
'''

def square_sum(list):
    
    result = 0
    for number in list:

        square = number ** 2
        result = result + square

    return result


# 9. Is he gonna survive?

'''
A hero is on his way to the castle to complete his mission. However, he's been 
told that the castle is surrounded with a couple of powerful dragons! 
Each dragon takes 2 bullets to be defeated, our hero has no idea how many 
bullets he should carry.. Assuming he's gonna grab a specific given number of 
bullets and move forward to fight another specific given number of dragons, 
will he survive?

Return True if yes, False otherwise :)
'''

def hero(bullets, dragons):

    bullets_needed = dragons * 2
    if bullets >= bullets_needed:
        return True
    else:
        return False


# 10. Even or odd

'''
Create a function (or write a script in Shell) that takes an integer as an 
argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    
    if 0 == int(number) % 2:
        return 'Even'
    else:
        return 'Odd'


# 11. Volume of a cuboid

'''
Bob needs a fast way to calculate the volume of a cuboid with three values: 
length, width and the height of the cuboid. Write a function to help Bob with 
this calculation.
'''

def get_cuboid_volume(length, width, height):
    return float(length * width * height)


# 12. Convert a number to string

'''
We need a function that can transform a number into a string.

What ways of achieving this do you know?

Examples:
number_to_string(123) /* returns '123' */
number_to_string(999) /* returns '999' */
'''

def number_to_string(number):
    return str(number)


# 13. Reversed sequence

'''
Details
Solutions
Forks (4)
Discourse (108)
Add to Collection|Share this kata:
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
'''

def reverse_seq(n):

    sequence = [n]
    index = n
    while index > 1:

        index = index - 1
        sequence.append(index)

    return sequence


## TEST CASES
if __name__ == '__main__':

    # 1. Remove First and Last Character
    assert remove_char('eloquent') == 'loquen'
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''

    # 2. The Feast of Many Beasts
    assert feast("great blue heron", "garlic naan") == True
    assert feast("chickadee", "chocolate cake") == True
    assert feast("brown bear", "bear claw") == False

    # 3. Transportation on vacation
    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270

    # 4. String repeat
    assert repeatStr(4, 'a') ==  'aaaa'
    assert repeatStr(3, 'hello ') == 'hello hello hello '
    assert repeatStr(2, 'abc') == 'abcabc'

    # 5. Rock Paper Scissors!
    assert rock_paper_scirrors('rock', 'scissors') == "Player 1 won!"
    assert rock_paper_scirrors('scissors', 'paper') == "Player 1 won!"
    assert rock_paper_scirrors('paper', 'rock') == "Player 1 won!"

    # 6. Double char
    assert double_char("String") =="SSttrriinngg"
    assert double_char("Hello World") =="HHeelllloo  WWoorrlldd"
    assert double_char("1234!_ ") =="11223344!!__  "

    # 7. Remove exclamation marks
    assert remove_exclamation_marks("Hello World!") == "Hello World"
    assert remove_exclamation_marks("Hello World!!!") == "Hello World"
    assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
    assert remove_exclamation_marks("") == ""
    assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"
    
    # 8. Square(n) sum
    assert square_sum([1,2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50

    # 9. Is he gonna survive?
    assert hero(10, 5) == True
    assert hero(7, 4) == False
    assert hero(4, 5) == False
    assert hero(100, 40) == True
    assert hero(1500, 751) == False
    assert hero(0, 1) == False

    # 10. Even or odd
    assert even_or_odd(2) == "Even"
    assert even_or_odd(0) == "Even"
    assert even_or_odd(7) == "Odd"
    assert even_or_odd(1) == "Odd"
    assert even_or_odd(-1) == "Odd"

    # 11. Volume of a cuboid
    assert get_cuboid_volume(1, 2, 2) == 4
    assert get_cuboid_volume(6.3, 2, 5) == 63

    # 12. Convert a number to string
    assert number_to_string(67) == '67'
    assert number_to_string(0) == '0'
    assert number_to_string(999) == '999'

    # 13. Reversed sequence
    assert reverse_sequence(5) == [5,4,3,2,1]
    assert reverse_sequence(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    