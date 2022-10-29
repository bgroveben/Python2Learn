class Calculator:
    "Execute simple math operations"

    def __init__(self, x, y, op="+"):
        """
        x -> int
        y -> int
        op -> +,-,*,/

        Performs addition, subtraction, multiplication, and division.
        Returns result as a float.

        >>> from Calculator import Calculator
        >>> d = Calculator(2,3,'+')
        >>> d.result
        5.0
        """
        try:
            int(x) and int(y)
            if op == "+":
                self._result = x + y
            elif op == "-":
                self._result = x - y
            elif op == "*":
                self._result = x * y
            elif op == "/":
                self._result = round(x / y)
            else:
                raise Exception("Operation must be +, -, *, or /.")
        except ValueError:
            print("x and y must be numbers")


    @property
    def result(self):
        return float(self._result)
