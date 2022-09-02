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
import time
import json
import random


def valid_len(n):
    if n.isnumeric():
        return int(n) in range(5,9)
    else:
        return False


def set_word_length():
    # When you run anagram_hunt.py in the console, you should be prompted to enter a word length:
    global word_length
    word_length = input("Please enter a word length [5, 6, 7, 8]:")
    # If you do not enter a correct word length, you should get an error message and a prompt to enter a word length again:
    while not valid_len(word_length):
        word_length = input("That is not an option. Please enter a word length [5, 6, 7, 8]:")
    print(word_length)
    return word_length


def play_again():
    replay = input("Play again? y/n ")
    if replay == "y":
        play_game()
    elif replay == "n":
        print("Goodbye")
    else:
        print("I don't get it. Goodbye")


def read_anagrams(word_length):
    """
    Randomly chooses a list of the user's chosen length and removes each word and list until the list of lists is empty.
    TODO:
    Compare user input to chosen word. If input matches a word in the inner list, remove it.
    Don't forget about the timer.
    """
    with open('data/anagrams.json', 'r') as f:
        data = f.read()
    anagrams = json.loads(data)
    outer_list = anagrams[str(word_length)]
    return outer_list


def play_game():
    """As soon as you enter a correct word length, the game should start"""
    set_word_length()
    outer_list = read_anagrams(word_length)
    score = 0
    start = time.time()
    """A timer should start counting down from 60 by 1 every second."""
    game_length = 10
    for l in range(len(outer_list)):
        random_inner = outer_list[random.randrange(len(outer_list))]
        random_word = random_inner[random.randrange(len(random_inner))]
        anagrams_guessed = []
        anagrams_guessed.append(random_word)
        while len(random_inner) > 1:
            print("Anagrams for : " + random_word)
            """Every time a message is logged to the console, the value of the timer should be checked and displayed."""
            user_input = input("Enter a word: ")
            time_check = time.time()
            print("Time Elapsed: " + str(time.time() - start))
            if time.time() - start >= game_length:
                print()
                print("Time's Up")
                print()
                print("Final Score : " + str(score))
                print()
                play_again()
                return None
            elif user_input == random_word:
                print("That's the word you were given")
            elif user_input in anagrams_guessed:
                print("Already guessed")
            elif user_input in random_inner:
                anagrams_guessed.append(user_input)
                print("anagrams_guessed: ")
                print(anagrams_guessed)
                print()
                random_inner.remove(user_input)
                print("random_inner: ")
                print(random_inner)
                print()
                score += 1
                print("Score : " + str(score))
                print()
            else:
                print("Not an anagram")
        outer_list.remove(random_inner)
    print()
    print("outer_list:")
    print(outer_list)
    print()


play_game()
