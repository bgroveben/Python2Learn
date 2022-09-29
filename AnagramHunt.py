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


class AnagramHunt:
    """
    Set attributes and write methods for Anagram Hunt Game
    Keyword arguments --
    -- wordlist    -> array
    -- outer_list  -> array
    -- anagram     -> str
    -- answer      -> str
    -- word_length -> str
    """
    def __init__(self, wordlist, outer_list, anagram, answer, word_length):
        self._wordlist = wordlist
        self._outer_list = outer_list
        self._anagram = anagram
        self._answer = answer
        self._word_length = word_length


    @classmethod  # cls instead of self, class v static methods
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
        """
        Sets and returns word length
        """
        self._word_length = input("Please enter a word length [5, 6, 7, 8]:")
        while not self.valid_len(self._word_length):
            length = input("That is not an option. Please enter a word length [5, 6, 7, 8]:")
        return self._word_length


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
        self._outer_list = self._wordlist[str(word_length)]
        return self._outer_list


    @classmethod
    def gameplay(self):
        """
        Chooses words and handles user input
        -- anagrams_guessed -> array
        -- score            -> int
        -- start            -> time object
        Returns None when time has expired
        """
        anagrams_guessed = []
        score = 0
        start = time.time()
        game_length = 10  # hard-coded for assignment
        for ary in range(len(self._outer_list)):
            random_inner = self._outer_list[random.randrange(len(self._outer_list))]
            self._anagram = random_inner[random.randrange(len(random_inner))]
            anagrams_guessed = []
            anagrams_guessed.append(self._anagram)
            while len(random_inner) > 1:
                print()
                print("random_inner: ")
                print(random_inner)
                print()
                print("Anagrams for : " + self._anagram)
                self._answer = input("Enter a word: ")
                time_check = "You have " + str(round(game_length - (time.time() - start),1)) + " seconds left."
                if time.time() - start > game_length:
                    print()
                    print("Time's Up")
                    print("Final Score : " + str(score))
                    return None
                elif self._answer == self._anagram:
                    print("That's the word you were given")
                    print(time_check)
                elif self._answer in anagrams_guessed:
                    print("Already guessed")
                    print(time_check)
                elif self._answer in random_inner:
                    anagrams_guessed.append(self._answer)
                    print("anagrams_guessed: ")
                    print(anagrams_guessed)
                    random_inner.remove(self._answer)
                    score += 1
                    print("Score : " + str(score))
                    print(time_check)
                    print()
                else:
                    print("Not an anagram")
                    print(time_check)
            try:
                self._outer_list.remove(random_inner)
            except IndexError:  # outer list is empty
                print()
                print("You guessed all of the anagrams!")
                print("Final Score : " + str(score))
                return None
