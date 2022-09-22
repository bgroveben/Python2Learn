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


class AnagramHunt:
    """
    Set attributes and write methods for Anagram Hunt Game
    Keyword arguments --
    -- wordlist -> array
    -- anagram  -> str
    -- answer   -> str
    """
    def __init__(self, wordlist, anagram, answer):
        self._wordlist = wordlist   #or self._wordlist = []
        self._anagram = anagram
        self._answer = answer


    @classmethod
    def valid_len(self, n):
        """
        User must choose a word length between 5 and 8 (inclusive)
        """
        if n.isnumeric():
            return int(n) in range(5,9)
        else:
            return False


    @classmethod
    def set_word_length(self):
        # When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
        word_length = input("Please enter a word length [5, 6, 7, 8]:")
        # If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
        while not self.valid_len(word_length):
            word_length = input("That is not an option. Please enter a word length [5, 6, 7, 8]:")
        print(word_length)
        return word_length


    @classmethod
    def read_anagrams(self, word_length):
        """
        Reads json file containing a dictionary of nested arrays
        Keyword argument --
        -- word_length -> int(n) in range(5,9)
        Returns outer array containing inner arrays of n-letter words
        """
        with open('data/anagrams.json', 'r') as f:
            data = f.read()
        self._wordlist = json.loads(data)
        outer_list = self._wordlist[str(word_length)]
        return outer_list
