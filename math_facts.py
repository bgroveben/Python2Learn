
"""
When you run math_facts.py in the console, you should be prompted to enter an operation:
>>>Please enter an operation [+, -, x, /]:

If you do not enter a correct operation, you should get an error message and a prompt to enter an operation again:
>>>That is not a correct operation. Please try again [+, -, x, /]:

As soon as you enter a correct operation, you should be prompted for a max number:
>>>Please enter a max number between 1 and 100:

If an invalid number is entered, you should get an error message and another prompt.
Once you have selected a valid operation and max number, the game should start.
A timer should start counting down from 30 by 1 every second.
Every time a message is logged to the console, the value of the timer should be checked and displayed.
A random problem with the selected operation and numbers below the max number should display:
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
import random
import time


def valid_op(s):
    return s in ['+','-','x','/']


def choose_operation():
    # When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
    operation = input("Please enter an operation [+, -, x, /]:")
    # If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
    while not valid_op(operation):
        operation = input("That is not a correct operation. Please try again [+, -, x, /]:")
    print(operation)
    return operation


def valid_num(n):
    # If an invalid number is entered, you should get an error message and another prompt.
    if n.isnumeric():
        return float(n) in range(1,101)
    else:
        return False


def set_max_num():
    # As soon as you enter a correct operation, you should be prompted for a max number
    max_num = input("Please enter a max number between 1 and 100:")
    while not valid_num(max_num):
        max_num = input("That is not a valid entry. Choose a number between 1 and 100:")
    return int(max_num)


def do_math(x, operation, y, score):
    game_length = 10
    while time.time() - start < game_length-1:
        if operation == '+':
            result = int(x + y)
        elif operation == '-':
            x,y = max(x,y),min(x,y)
            result = int(x - y)
        elif operation == 'x':
            result =  int(x * y)
        elif operation == '/':
            # Try something more elegant:
            x,y = max(x,y),min(x,y)
            result = x / y
            """
            >>>Please enter a max number between 1 and 100:100
            >>>2.6944444444444446
            >>>2.7, CH3@T3R ;)
            >>>97 / 36 = ?: 2.7
            >>>Correct!
            """
        print()
        print("Time left: " + str(round(game_length - (time.time() - start))))
        result = round(result,1)
        print(result)
        try:
            answer = float(input(f"{x} {choose_operation} {y} = ?: "))
        except ValueError:
            print("Please enter a number.")
            do_math(x, choose_operation, y, score)
        try:
            if time.time() - start > game_length-1:
                print("Time's Up")
            elif answer == result:
                print("Correct!")
                score += 1
                print("Score: " + str(score))
                x = random.randint(1, set_max_num)
                y = random.randint(1, set_max_num)
                do_math(x, choose_operation, y, score)
            else:
                print(f"{int(answer)} is not correct. Try again.")
                do_math(x, choose_operation, y, score)
        except UnboundLocalError:
            break
        break


def main():
    global choose_operation
    choose_operation = choose_operation()
    global set_max_num
    set_max_num = set_max_num()
    global score
    score = 0
    global start
    start = time.time()
    x = random.randint(1, set_max_num)
    y = random.randint(1, set_max_num)
    do_math(x, choose_operation, y, score)


main()
