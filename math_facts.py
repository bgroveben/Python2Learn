import random
import time
from MathFacts import MathFacts
from Calculator import Calculator


operation = MathFacts.choose_op()
maximum = MathFacts.set_max_num()
game_length = 10
start = time.time()


def run_game():
    if time.time() - start > (game_length + 1):
        print(round((time.time() - start),1))
        print("Game Over")
        return None
    do_math(maximum, operation)


def do_math(maximum, operation):
    x = random.randint(1, maximum)
    y = random.randint(1, maximum)
    equation = f"{x} {operation} {y} = ?: "
    answer = Calculator(x,y,operation).result
    print(round((time.time() - start),1))
    print(equation)
    print(answer)
    check_answer(answer)


def is_number(n):
    if n.isnumeric():
        return n
    else:
        return False


def validate_input():
    user_answer = input("Enter an answer: ")
    while not is_number(user_answer):
        if time.time() - start > (game_length + 1):
            print(round((time.time() - start),1))
            print("Game Over")
            return None
        user_answer = input("Invalid Entry. Enter an answer: ")
    return user_answer


def check_answer(result):
    user_answer = validate_input()
    try:
        while float(user_answer) != float(result):
            print(f"{user_answer} is not correct. Try again.")
            if time.time() - start > (game_length + 1):
                print(round((time.time() - start),1))
                print("Game Over")
                return None
            user_answer = validate_input()
        else:
            print("Correct")
            run_game()
    except TypeError:
        return None


def main():
    run_game()


if __name__ == '__main__':
    main()
