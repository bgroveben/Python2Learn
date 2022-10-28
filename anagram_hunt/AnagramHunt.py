import json
import random
import time
from threading import Timer


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
            cls._word_length = input(
            "That is not a correct word length. Please try again [5, 6, 7, 8]:"
            )
        return cls._word_length


    @classmethod
    def read_anagrams(cls, word_length):
        """
        Reads json file containing a dictionary of nested arrays
        word_length -> int(n) in range(5,9)
        Returns outer array containing inner arrays of n-letter words
        """
        with open('../data/fewer_anagrams.json', 'r') as f:
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
        print(
        f"You got {cls._score} anagrams for {cls._word_length}-letter words!"
        )
        print()


    @classmethod
    def gameplay(cls):
        """
        Chooses words and handles user input
        Calls game_over() if user has guessed all anagrams
        Returns None if time runs out
        """
        anagrams_guessed = []
        cls._score = 0
        start = time.time()
        cls._game_length = 45  # hard-coded for assignment
        cls._game_on = True
        cls._timer = Timer(cls._game_length - 0.5, cls.timeout)
        # Why cheat the user out of one half second?
        # So the console doesn't display:
        # -> You have 0 seconds left.
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
                print("You have " + str(round(cls._game_length -
                     (time.time() - start))) + " seconds left.")
                print(f"The word is: {cls._anagram.upper()}")
                if len(random_inner) == 2:
                    print("There is 1 unguessed anagram left.")
                else:
                    print(
                    f"There are {len(random_inner)-1} unguessed anagrams left."
                    )
                cls._answer = input("Make a guess: ")
                print()
                if time.time() - start >= cls._game_length - 0.5:
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
                        print(
                        f"You got all the anagrams for {cls._anagram.upper()}!"
                        )
                else:
                    print(f"{cls._answer.upper()} is not a valid anagram. Please try again.")
            else:
                cls._outer_list.remove(random_inner)
        cls.game_over()


    @classmethod
    def timeout(cls):
        """
        Tells user that they are out of time and displays score
        User has to hit Enter twice to continue, so that they don't
        unintentionally restart the game
        """
        print("\n")
        print("Time is up!")
        print()
        print("Sorry, you didn’t get that answer in on time.")
        print()
        if cls._score == 1:
            print(f"You answered {cls._score} problem!")
        else:
            print(f"You answered {cls._score} problems!")
        print()
        print("Press Enter to continue...")
