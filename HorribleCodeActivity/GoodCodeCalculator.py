class Calculator:

    def add(self, A, B):
        # This function will return the sum of A and B.
        return A + B

    def subtract(self, A, B):
        # This function will return the difference of A and B.
        return A - B

    def multiply(self, A, B):
        # This function will return the product of A and B.
        return A * B

    def divide(self, A, B):
        # This function will return the quotient of A and B, except when y is a zero.
        if B == 0:
            return "error: cannot divide by 0"
        return A / B

# Instances to check my code
calc = Calculator()
print(calc.add(120, 92))       # This calculates 120 + 92
print(calc.subtract(129, 45))    # This calculates 129 - 45
print(calc.multiply(23, 12))  # This calculates 23 * 12
print(calc.divide(8, 2))          # This calculates 8 / 2
print(calc.divide(8, 0))          # This calculates 8 / 0
