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
