import random
import time
from MathFacts import MathFacts

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

def replay():
    print()
    replay = input("Press Enter to play again.")
    if replay == "":
        start = time.time()
        main()
    else:
        print("Thank you for playing. Goodbye.")
        return None


def main():
    MathFacts.choose_op()
    MathFacts.set_max_num()
    MathFacts.run_game()
    replay()


if __name__ == '__main__':
    main()
