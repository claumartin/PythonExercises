class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score


    @staticmethod
    def yatzy(*dice):
        reference = dice[0]
        for die in dice:
            if die != reference:
                return 0        
        return 50
    

    @staticmethod
    def ones(*dice):
        score = dice.count(1)
        return score
    
    @staticmethod
    def twos( *dice):
        score = dice.count(2) * 2
        return score
    
    @staticmethod
    def threes( *dice):
        score = dice.count(3) * 3
        return score

    @staticmethod
    def fours(*dice):
        score = dice.count(4) * 4
        return score

    @staticmethod
    def fives(*dice):
        score = dice.count(5) * 5
        return score
    
    @staticmethod
    def sixes(*dice):
        score = dice.count(6) * 6
        return score
    

    @staticmethod
    def pair(*dice):
        matchedDice = []
        for die in dice:
            if dice.count(die) > 1:
                matchedDice.append(die)
        if matchedDice != []:    
            maxDie = max(matchedDice)
            return maxDie * 2
        else:
            return 0
    
    @staticmethod
    def two_pairs(*dice):
        matchedDice = []
        for die in dice:
            if dice.count(die) > 1 and die not in matchedDice:
                matchedDice.append(die)
        score = 0
        if len(matchedDice) > 1:
            for die in matchedDice:
                score += die * 2
        return score
    

    @staticmethod
    def three_of_a_kind(*dice):
        score = 0
        for die in dice:
            if dice.count(die) >= 3:
                score = die * 3
        return score

    @staticmethod
    def four_of_a_kind(*dice):
        score = 0
        for die in dice:
            if dice.count(die) >= 4:
                score = die * 4 
        return score   
    

    @staticmethod
    def small_straight(*dice):
        for number in range(1, 6):
            if dice.count(number) != 1:
                return 0
        return 15
    
    @staticmethod
    def large_straight(*dice):
        for number in range(2, 7):
            if dice.count(number) != 1:
                return 0
        return 20
    

    @staticmethod
    def full_house(*dice):
        trio = 0
        pair = 0
        for die in dice:
            if dice.count(die) == 3:
                trio = 3
            elif dice.count(die) == 2:
                pair = 2
        if trio == 3 and pair == 2:
            return 18
        else:
            return 0