class Calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        result = None
        if self.operator == '+':
            result = float(self.num1 + self.num2)
        elif self.operator == '-':
            result = float(self.num1 - self.num2)
        elif self.operator == '*':
            result = float(self.num1 * self.num2)
        elif self.operator == '/':
            if self.num2 != 0:
                result = float(self.num1 / self.num2)
            else: return "You cannot divide by 0"
        return result

c = Calculator (10.352, 5.234, "/")
print (c.calculate())
