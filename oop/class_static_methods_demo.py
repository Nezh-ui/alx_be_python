class Calculator:
    calculation_type = "Arithmetic operations"
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls,a, b):
        return a * b
    def __init__(self, calculation_type):
        self.calculation_type = calculation_type
