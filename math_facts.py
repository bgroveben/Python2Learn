
"""
When you run math_facts.py in the console, you should be prompted to enter an op:
>>>Please enter an op [+, -, x, /]:

If you do not enter a correct op, you should get an error message and a prompt to enter an op again:
>>>That is not a correct op. Please try again [+, -, x, /]:

As soon as you enter a correct op, you should be prompted for a max number:
>>>Please enter a max number between 1 and 100:

If an invalid number is entered, you should get an error message and another prompt.
Once you have selected a valid op and max number, the game should start.
A timer should start counting down from 30 by 1 every second.
Every time a message is logged to the console, the value of the timer should be checked and displayed.
A random problem with the selected op and numbers below the max number should display:
>>>5 x 5 = ?
>>>You have 30 seconds left.
>>>Enter an answer:

If the answer is incorrect, you should get an error and a prompt:
>>>26 is not correct. Try again! 5 x 5 =?
>>>You have 28 seconds left.
>>>Enter an answer:

If the answer is correct, it should tell you and display a new problem:
>>>25 is correct!
>>>3 x 5 = ?
>>>You have 24 seconds left.
>>>Enter an answer:

The game should end when the time runs out:
>>>Time is up!
>>>Sorry, you didn’t get that answer in on time.
>>>You answered 15 problems!
>>>Press Enter to play again.
"""
# Advanced Python -- Extending a class method.
# classes-objects/Demos/extending_a_class_method.py -- change print statement
# Display different messages to user. (Maybe use a decorator)
# Class attributes and Methods -- MyCounter.py to keep score
# Static method (@staticmethod) for validating op and num
# Game class (abstract) that has attributes and methods for both games
# -- both games have a score and a timer

# Message to user with time left, score, and results:
# Maybe use a decorator to:
# Print a couple of lines of text.
# Run the passed-in function. -- call time remaining function.
# Print another couple of lines of text

# make op a class attribute?
# Class attributes can also sometimes be used to provide default attribute values, like game_over = False

import random
from Calculator import Calculator
from Evaluator import Evaluator
from ScoreKeeper import ScoreKeeper

def valid_op(s):
    return s in ['+','-','*','/']

def choose_op():
    # When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
    op = input("Please enter an operation [+, -, *, /]:")
    # If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
    while not valid_op(op):
        op = input("That is not a valid operation. Please try again [+, -, *, /]:")
    return op

def valid_num(n):
    # If an invalid number is entered, you should get an error message and another prompt.
    if n.isnumeric():
        return float(n) in range(1,101)
    else:
        return False

def set_max_num():
    # As soon as you enter a correct op, you should be prompted for a max number
    max_num = input("Please enter a max number between 1 and 100:")
    # If an invalid number is entered, you should get an error message and another prompt.
    while not valid_num(max_num):
        max_num = input("That is not a valid entry. Choose a number between 1 and 100:")
    return int(max_num)


def change_equation(max_num, op):
    x = random.randint(1, max_num)
    y = random.randint(1, max_num)
    equation = f"{x} {op} {y} = ?: "
    answer = Calculator(x,y,op).result
    print(equation)
    print(answer)
    output = Evaluator(answer).user_input


def main():
    op = choose_op()
    max_num = set_max_num()
    x = random.randint(1, max_num)
    y = random.randint(1, max_num)
    equation = f"{x} {op} {y} = ?: "
    answer = Calculator(x,y,op).result
    print(equation)
    print(answer)
    output = Evaluator(answer).user_input
    print(output)
    while output:
        change_equation(max_num, op)


if __name__ == '__main__':
    main()
