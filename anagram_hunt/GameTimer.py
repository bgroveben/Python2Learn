from threading import Timer

class GameTimer:
    """
    As soon as you enter a correct word length, the game should start:
    A timer should start counting down from 60 by 1 every second.
    Every time a message is logged to the console, the value of the timer
    should be checked and displayed.
    The game should end when the timer runs out or when you get through all
    of the anagram sets for the specified length. If you check the time and
    it is up, you can display a message like this:
    >>> Time is up!
    >>> You got 7 anagrams for 5-letter words!
    >>> Press Enter to play again.
    If the time is already up when you submit an answer, you should get a
    message like this:
    >>> Time is up!
    >>> Sorry, you didn’t get that last one in on time.
    >>> You got 7 anagrams for 5-letter words!
    >>> Press Enter to play again.
    """
    # The timer in AnagramHunt works, but it doesn't interrupt the user input when time runs out.
    def times_up():
        print()
        print("Time is up!")
        print("You got 7 anagrams for 5-letter words!")
        print("Press Enter to continue")

    t = Timer(10, times_up)
    t.start()
    answer = input("What is the answer?")
    print(t.interval) # Does interval stay at 10, or does it count down?



# SuperFastPython.com
# example of using a thread timer object
#from threading import Timer
# target task function
#def task(message):
    # report the custom message
    #print(message)
    #raise Exception("Game Over")

# create a thread timer object
#timer = Timer(3, task, args=('Hello world',))
# start the timer object
#timer.start()
# wait for the timer to finish
#print('Waiting for the timer...')
