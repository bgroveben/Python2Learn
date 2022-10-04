import random
import time
from Calculator import Calculator

class MathFacts:
    """
    Contains class methods that run the game.
    """

    @classmethod
    def valid_op(cls, s):
        """
        Validate user input for op
        """
        return s in ['+','-','*','/']


    @classmethod
    def choose_op(cls):
        """
        Allows user to choose operation
        """
        cls._op = input("Please enter an operation [+, -, *, /]:")
        while not cls.valid_op(cls._op):
            cls._op = input("That is not a valid operation. Please try again [+, -, *, /]:")
        return cls._op


    @classmethod
    def valid_num(cls, n):
        """
        Validates user input for max_num
        """
        if n.isnumeric():
            return float(n) in range(1,101)
        else:
            return False


    @classmethod
    def set_max_num(cls):
        """
        Allows user to set max number for math operations
        """
        cls._max_num = input("Please enter a max number between 1 and 100:")
        while not cls.valid_num(cls._max_num):
            cls._max_num = input("That is not a valid entry. Choose a number between 1 and 100:")
        return int(cls._max_num)


    @classmethod
    def do_math(cls, start):
        """
        Generates an equation based on game parameters,
        then calls check_answer()
        """
        if time.time() - cls._start > (cls._game_length):
            print(round((time.time() - cls._start),1))
            print("Game Over")
            return None
        x = random.randint(1, int(cls._max_num))
        y = random.randint(1, int(cls._max_num))
        if cls._op == '-' or cls._op == '/':
            x,y = max(x,y), min(x,y)
        equation = f"{x} {cls._op} {y} = ?: "
        answer = Calculator(x,y,cls._op).result
        print(round((time.time() - cls._start),1))
        print(equation)
        print(answer)
        cls.check_answer(answer)


    @classmethod
    def check_answer(cls, result):
        """
        Checks to see if user input for answer matches equation
        If question and answer match, call do_math() until time expires
        """
        user_answer = cls.validate_input()
        try:
            while float(user_answer) != float(result):
                print(f"{user_answer} is not correct. Try again.")
                if time.time() - cls._start > (cls._game_length):
                    print(round((time.time() - cls._start),1))
                    print("Game Over")
                    return None
                user_answer = cls.validate_input()
            else:
                cls._score += 1
                print("Correct ", cls._score)
                cls.do_math(cls._start)
        except TypeError:
            print('TypeError')
            cls.do_math(cls._start)
            # return None


    @classmethod
    def validate_input(cls):
        """
        Gets answer from user, then validates input before returning
        user's answer
        """
        user_answer = input("Enter an answer: ")
        while not cls.is_number(user_answer):
            if time.time() - cls._start > (cls._game_length):
                print(round((time.time() - cls._start),1))
                print("Game Over")
                return None
            user_answer = input("Invalid Entry. Enter an answer: ")
        return user_answer


    @classmethod
    def is_number(cls, n):
        """
        Validates user input for answer
        """
        if n.isnumeric():
            return n
        else:
            return False


    @classmethod
    def run_game(cls):
        """
        Starts timer when called, then calls do_math() until time expires
        """
        cls._start = time.time()
        cls._game_length = 10
        cls._score = 0
        cls.do_math(cls._start)
        print(round((time.time() - cls._start),1))
