class Calculator:
    "Execute simple math operations"
    def __init__(self, x, y, op='+'):
        """
        x -> num
        y -> num
        op -> +,-,*,/

        Performs addition, subtraction, multiplication, and division.
        Returns the solution to the equation as an int or a float.

        >>> from Calculator import Calculator
        >>> d = Calculator(2,3,'+')
        >>> d.result
        5
        """
        try:
            int(x) and int(y)
            if op == '+':
                self._result = x + y
            elif op == '-':
                x,y = max(x,y), min(x,y)
                self._result = x - y
            elif op == '*':
                self._result = x * y
            elif op == '/':
                x,y = max(x,y), min(x,y)
                self._result = x / y
            else:
                raise Exception("Operation must be +, -, *, or /.")
        except ValueError:
            print("x and y must be numbers")


    @property
    def result(self):
        return self._result
