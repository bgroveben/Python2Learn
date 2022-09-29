import random
from MathFacts import MathFacts
from Calculator import Calculator
#from Evaluator import Evaluator


# from collections import namedtuple
#Point = namedtuple('Point', 'x, y')
# question = namedtuple('x', 'y', '+')

def do_math():
    operation = MathFacts.choose_op()
    maximum = MathFacts.set_max_num()
    x = random.randint(1, maximum)
    y = random.randint(1, maximum)
    equation = f"{x} {operation} {y} = ?: "
    answer = Calculator(x,y,operation).result
    print(equation)
    print(answer)
    return answer


def check_answer(result):
    try:
        user_answer = float(input("Enter an answer: "))
    except ValueError:
        print("Please enter a number")

    while user_answer != result:
        print(f"{user_answer} is not correct. Try again.")
        try:
            user_answer = float(input("Enter an answer: "))
        except ValueError:
            print("Please enter a number")
    else:
        print("Correct")


def main():
    problem = do_math()
    result = check_answer(problem)


if __name__ == '__main__':
    main()
