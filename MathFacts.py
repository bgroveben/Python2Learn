class MathFacts:
    """
    Contains class methods that allow user to set the game parameters for operation and maximum number.
    """
    @classmethod
    def valid_op(cls, s):
        return s in ['+','-','*','/']


    @classmethod
    def choose_op(cls):
        op = input("Please enter an operation [+, -, *, /]:")
        while not cls.valid_op(op):
            op = input("That is not a valid operation. Please try again [+, -, *, /]:")
        return op


    @classmethod
    def valid_num(cls, n):
        if n.isnumeric():
            return float(n) in range(1,101)
        else:
            return False


    @classmethod
    def set_max_num(cls):
        max_num = input("Please enter a max number between 1 and 100:")
        while not cls.valid_num(max_num):
            max_num = input("That is not a valid entry. Choose a number between 1 and 100:")
        return int(max_num)
