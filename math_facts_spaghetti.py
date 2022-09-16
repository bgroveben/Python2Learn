
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
import random
import time
# from Calculator import Calculator


def valid_op(s):
    return s in ['+','-','*','/']


def choose_op():
    # When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
    op = input("Please enter an operation [+, -, *, /]:")
    # If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
    while not valid_op(op):
        op = input("That is not a valid operation. Please try again [+, -, *, /]:")
    #print(op)
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


def play_again(x, op, y, score):
    replay = input("Play again? y/n ")
    if replay == "y":
        main()
    else:
        print("Goodbye")

# Lambda functions are anonymous functions that are generally used to complete a small task, after which they are no longer needed.
# f = lambda n: n**2
def do_math(x, op, y, score):
    # A timer should start counting down from 30 by 1 every second.
    game_length = 10
    while time.time() - start < game_length:
        try:
            int(x) and int(y)
            if op == '+':
                result = x + y
                #result = lambda x,y: x + y
            elif op== '-':
                x,y = max(x,y),min(x,y)
                result = x - y
                #result = lambda x,y: x - y
            elif op== '*':
                result = x * y
                #result = lambda x,y: x * y
            elif op== '/':
                x,y = max(x,y),min(x,y)
                result = x / y
                #result = lambda x,y: x / y
            else:
                raise Exception("op must be +, -, *, or /.")
        except ValueError:
            print("x and y must be numbers")
        print()
        result = round(result,1) # Answer to cheat, or sanity check
        print(result)
        print()
        try:
            # Every time a message is logged to the console, the value of the timer should be checked and displayed.
            # A random problem with the selected operation and numbers below the max number should display:
            print(f"{x} {op} {y} = ?: ")
            print("You have " + str(round(game_length - (time.time() - start))) + " seconds left")
            answer = float(input("Enter an answer: "))
            # The game should end when the time runs out:
            if time.time() - start > game_length:
                print("Time's Up")
                print("Sorry, the last one doesn't count.")
                print("Final Score : " + str(score))
                play_again(x, op, y, score)
            elif answer == result:
                # Every time a message is logged to the console, the value of the timer should be checked and displayed.
                print("Time left: " + str(round(game_length - (time.time() - start))))
                # If the answer is correct, it should tell you and display a new problem:
                print("Correct!")
                score += 1
                print("Score: " + str(score))
                x = random.randint(1, max_num)
                y = random.randint(1, max_num)
                do_math(x, op, y, score)
            # If the answer is incorrect, you should get an error and a prompt:
            while answer != result:
                print(f"{int(answer)} is not correct. Try again.")
                print(f"{x} {op} {y} = ?: ")
                # Every time a message is logged to the console, the value of the timer should be checked and displayed.
                print("You have " + str(round(game_length - (time.time() - start))) + " seconds left")
                answer = float(input("Enter an answer: "))
                # The game should end when the time runs out:
                if time.time() - start > game_length:
                    print("Time's Up")
                    print("Sorry, the last one doesn't count.")
                    print("Final Score : " + str(score))
                    play_again(x, op, y, score)
                    break
        except UnboundLocalError:
            break
        except ValueError:
            if time.time() - start > game_length:
                print("Time's Up")
                print("Sorry, the last one doesn't count.")
                print("Final Score : " + str(score))
                #break
                play_again(x, op, y, score)
            else:
                print("Please enter a number.")
                continue


def main():
    global op
    op = choose_op()
    global max_num
    max_num = set_max_num()
    # Once you have selected a valid operation and max number, the game should start.
    global score
    score = 0
    global start
    # A timer should start counting down from 30 by 1 every second.
    start = time.time()
    x = random.randint(1, max_num)
    y = random.randint(1, max_num)
    do_math(x, op, y, score)


main()
