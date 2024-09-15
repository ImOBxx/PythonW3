class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return a + b
    
    def sub(self):
        return a - b
    
    def mult(self):
        return a * b
    
    def div(self):
        return a // b
    
    def __str__(self):
        print()
        print("Calculations :- ")
        print()
        return (f"Addition: {self.add()}\n\n"
                f"Subtraction: {self.sub()}\n\n"
                f"Multiplication: {self.mult()}\n\n"
                f"Division: {self.div()}\n")


print()
print("Simple Calculator: ")    
print()
a = int (input ("Enter 1st Number: "))
b = int (input ("Enter 2nd Number: "))
print()

s1 = Calculator(a, b)
print(s1)