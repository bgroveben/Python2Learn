import time
from MathFacts import MathFacts


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
