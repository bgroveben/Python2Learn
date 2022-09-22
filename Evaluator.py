class Evaluator:
    """
    result -> result calculated by Calculator

    Compares user's answer to the correct answer.
    Returns True if they match.
    If answer is incorrect, user input prompt is repeated.
    """
    def __init__(self, result):
        self._result = result
        try:
            self._user_answer = float(input("Enter an answer: "))
        except ValueError:
            print("Please enter a number")

        while self._user_answer != result:
            print(f"{self._user_answer} is not correct. Try again.")
            self._user_answer = float(input("Enter an answer: "))
        else:
            print("Correct")


    @property
    def user_input(self):
        return self._user_answer == self._result
