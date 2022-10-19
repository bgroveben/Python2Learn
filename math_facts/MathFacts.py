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
        try:
            return int(n) in range(1,101)
        except ValueError:
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
        if time.time() - start >= (cls._game_length):
            cls.times_up()
            return None
        x = random.randint(1, int(cls._max_num))
        y = random.randint(1, int(cls._max_num))
        if cls._op == '-' or cls._op == '/':
            x,y = max(x,y), min(x,y)
        cls._equation = f"{x} {cls._op} {y} = ?: "
        answer = Calculator(x,y,cls._op).result
        print(cls._equation)
        print(answer)
        print("You have " + str(round(cls._game_length - (time.time() - start),1)) + " seconds left.")
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
                if time.time() - cls._start >= (cls._game_length):
                    cls.times_up()
                    return None
                print(f"{user_answer} is not correct. Try again! {cls._equation}")
                print("You have " + str(round(cls._game_length - (time.time() - cls._start),1)) + " seconds left.")
                user_answer = cls.validate_input()
            else:
                if time.time() - cls._start >= (cls._game_length):
                    cls.times_up()
                    return None
                cls._score += 1
                print(f"{user_answer} is correct!")
                print(f"Score: {cls._score}")
                print("You have " + str(round(cls._game_length - (time.time() - cls._start),1)) + " seconds left.")
                cls.do_math(cls._start)
        except TypeError:
            return None


    @classmethod
    def validate_input(cls):
        """
        Gets answer from user, then validates input before returning
        user's answer
        """
        user_answer = input("Enter an answer: ")
        while not user_answer.isnumeric():
            if time.time() - cls._start >= (cls._game_length):
                cls.times_up()
                return None
            print("You have " + str(round(cls._game_length - (time.time() - cls._start),1)) + " seconds left.")
            user_answer = input(f"Invalid Entry. Try again! {cls._equation}")
        return user_answer


    @classmethod
    def times_up(cls):
        """
        Tells user the game is over and displays the score
        """
        print("Time is up!")
        print("Sorry, you didn’t get that answer in on time.")
        if cls._score == 1:
            print(f"You answered {cls._score} problem!")
        else:
            print(f"You answered {cls._score} problems!")


    @classmethod
    def run_game(cls):
        """
        Starts timer when called, then calls do_math() until time expires
        """
        cls._start = time.time()
        cls._game_length = 10
        cls._score = 0
        cls._equation = ""
        cls.do_math(cls._start)
