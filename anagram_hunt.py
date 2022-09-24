"""
When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
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
from AnagramHunt import AnagramHunt


def play_again():
    """
    Lets user play again
    Calls main function to continue or returns None
    """
    replay = input("Press Enter to play again.")
    if replay == "":
        main()
    else:
        print("Thank you for playing. Goodbye.")
        return None


def main():
    num_letters = AnagramHunt.set_word_length()
    anagrams = AnagramHunt.read_anagrams(num_letters)
    AnagramHunt.gameplay()
    play_again()


if __name__ == '__main__':
    main()
