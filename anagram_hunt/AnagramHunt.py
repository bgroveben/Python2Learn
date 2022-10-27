"""
When you !*run anagram_hunt.py in the console*!, you should be prompted to enter a word length:
>>>Please enter a word length [5, 6, 7, 8]:

If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
>>>That is not a correct word length. Please try again [5, 6, 7, 8]:

As soon as you enter a correct word length, the game should start:
A timer should start counting down from 60 by 1 every second.
Every time a message is logged to the console, the value of the timer should be checked and displayed.
From an array of arrays similar to the one in this JavaScript file, you should grab a random list of words of the specified length.
From that list, display a random word.
You need to guess anagrams for this word:
>>>The word is: BEARD
>>>There are 3 unguessed anagrams.
>>>You have 60 seconds left.
>>>Make a guess:

If you type in an incorrect guess, you should get a warning and another prompt:
>>>BRAID is not a valid anagram. Please try again.
>>>The word is: BEARD
>>>There are 3 unguessed anagrams.
>>>You have 55 seconds left.
>>>Make a guess:

If you guess a correct anagram, it should tell you and prompt you again:
>>>BREAD is correct!
>>>The word is: BEARD
>>>There are 2 unguessed anagrams.
>>>You have 49 seconds left.
>>>Make a guess:

If you guess a word that you have already gotten, you should get a warning and another prompt:
>>>You already got BREAD. Try again.
>>>The word is: BEARD
>>>There are 2 unguessed anagrams.
>>>You have 44 seconds left.
>>>Make a guess:

If you get all the anagrams for a word, a new word should be displayed:
>>>You got all the anagrams for BEARD!
>>>The word is: REACT
>>>There are 4 unguessed anagrams.
>>>You have 38 seconds left.
>>>Make a guess:

The game should end when the timer runs out or when you get through all of the anagram sets for the specified length.
If you check the time and it is up, you can display a message like this:
>>>Time is up!
>>>You got 7 anagrams for 5-letter words!
>>>Press Enter to play again.

If the time is already up when you submit an answer, you should get a message like this:
>>>Time is up!
>>>Sorry, you didn’t get that last one in on time.
>>>You got 7 anagrams for 5-letter words!
>>>Press Enter to play again.

"""
import json
import random
import time
from threading import Timer
from pynput.keyboard import Key, Controller


class AnagramHunt:
    """
    Contains class methods that run the game.
    """

    @classmethod
    def valid_len(cls, n):
        """
        User must choose a word length between 5 and 8 (inclusive)
        """
        return n.isnumeric() and 5 <= int(n) <= 9


    @classmethod
    def set_word_length(cls):
        """
        Sets and returns word length
        """
        cls._word_length = input("Please enter a word length [5, 6, 7, 8]:")
        while not cls.valid_len(cls._word_length):
            cls._word_length = input("That is not a correct word length. Please try again [5, 6, 7, 8]:")
        return cls._word_length


    @classmethod
    def read_anagrams(cls, word_length):
        """
        Reads json file containing a dictionary of nested arrays
        word_length -> int(n) in range(5,9)
        Returns outer array containing inner arrays of n-letter words
        """
        with open('../data/anagrams_test.json', 'r') as f:
            data = f.read()
        cls._wordlist = json.loads(data)
        cls._outer_list = cls._wordlist[str(word_length)]
        return cls._outer_list


    @classmethod
    def game_over(cls):
        """
        Cancels game timer, congratulates user, and displays score
        """
        cls._timer.cancel()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You guessed all of the anagrams!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"You got {cls._score} anagrams for {cls._word_length}-letter words!")
        print()


    @classmethod
    def gameplay(cls):
        """
        Chooses words and handles user input
        Continues until user has guessed all anagrams or timer expires
        """
        anagrams_guessed = []
        cls._score = 0
        start = time.time()
        cls._game_length = 45  # hard-coded for assignment
        cls._game_on = True
        cls._timer = Timer(cls._game_length, cls.timeout)
        cls._timer.start()
        for ary in range(len(cls._outer_list)):
            random_inner = cls._outer_list[random.randrange(len(cls._outer_list))]
            cls._anagram = random_inner[random.randrange(len(random_inner))]
            anagrams_guessed = []
            anagrams_guessed.append(cls._anagram)
            while len(random_inner) > 1 and cls._game_on == True:
                print()
                print(f"{random_inner} Ch3@t3r")
                print()
                time_check = "You have " + str(round(cls._game_length - (time.time() - start),1)) + " seconds left."
                print(f"The word is: {cls._anagram.upper()}")
                if len(random_inner) == 2:
                    print("There is 1 unguessed anagram left.")
                else:
                    print(f"There are {len(random_inner)-1} unguessed anagrams left.")
                print(time_check)
                cls._answer = input("Make a guess: ")
                print()
                if time.time() - start >= cls._game_length:
                    # stops Enter key from continuing current game
                    return None
                elif cls._answer == cls._anagram:
                    print(f"{cls._anagram.upper()} is the word you were given. Try again.")
                elif cls._answer in anagrams_guessed:
                    print(f"You already got {cls._answer.upper()}. Try again.")
                elif cls._answer in random_inner:
                    anagrams_guessed.append(cls._answer)
                    cls._score += 1
                    print(f"{cls._answer.upper()} is correct!")
                    random_inner.remove(cls._answer)
                    if len(random_inner) == 1:
                        print(f"You got all the anagrams for {cls._anagram.upper()}!")
                else:
                    print(f"{cls._answer.upper()} is not a valid anagram. Please try again.")
            else:
                cls._outer_list.remove(random_inner)
        cls.game_over()


    @classmethod
    def timeout(cls):
        """
        Tells user that they are out of time, and interrupts keyboard input
        so that replay() works in main().
        This code could inherit any bugs that come with pynput.
        # https://pypi.org/project/pynput/
        # https://xkcd.com/353/
        """
        print("\n")
        print("Time is up!")
        print()
        print("Sorry, you didn’t get that last one in on time.")
        print()
        if cls._score == 1:
            print(f"You got {cls._score} anagram for {cls._word_length}-letter words")
        else:
            print(f"You got {cls._score} anagrams for {cls._word_length}-letter words")
        keyboard = Controller()
        keyboard.press(Key.enter)
        print("*********************************************")
