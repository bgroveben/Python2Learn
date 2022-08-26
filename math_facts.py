
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


def valid_op(s):
    return s in ['+','-','x','/','//']


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
        return int(n) in range(1,101)
    else:
        return False


def set_max_num():
    # As soon as you enter a correct operation, you should be prompted for a max number
    max_num = input("Please enter a max number between 1 and 100:")
    while not valid_num(max_num):
        max_num = input("That is not a valid entry. Choose a number between 1 and 100:")
    return int(max_num)


def do_math(x, operation, y):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == 'x':
        result =  x * y
    elif operation == '/':
        """
        Please enter a max number between 1 and 100:99
        >>>1.0416666666666667
        >>>1.0, CH3@T3R ;)
        >>>50 / 48 = ?: 1
        >>>right
        ???
        """
        # Only return numbers with no remainder using modulo
        #if max(x,y) % min(x,y) == 0:
        #while max(x,y) % min(x,y) != 0:
        result = max(x,y) / min(x,y)
        #else:
            #x = random.randint(1, set_max_num)
            #y = random.randint(1, set_max_num)

    print(result)
    return result


def get_results():
    answer = float(input(f"{x} {choose_operation} {y} = ?: "))
    if answer == round(do_math,1):
        results = "right"
        # score +=1
    elif answer == float(round(do_math,1)) or answer == int(round(do_math,1)):
        results = "int or float"
    else:
        results = "wrong" # + timer
    print(results)


# Put the following in a main function
choose_operation = choose_operation()
set_max_num = set_max_num()
x = random.randint(1, set_max_num)
y = random.randint(1, set_max_num)
x,y = max(x,y),min(x,y)
do_math = do_math(x, choose_operation, y)
# sanity check
cheater = round(do_math,1)
print(f"{cheater}, CH3@T3R ;) ")
get_results()
