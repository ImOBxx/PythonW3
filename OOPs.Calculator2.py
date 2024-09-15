class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mult(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def __str__(self):
        if choice == " + ":
            return (f"{self.a} + {self.b} = {(self.add())}")
        elif choice == " - ":
            return  (f"{self.a} - {self.b} = {(self.sub())}")
        elif choice == " * ":
            return  (f"{self.a} * {self.b} = {(self.mult())}")
        elif choice == " / ":
            return  (f"{self.a} / {self.b} = {(self.div())}")
        else:
            return "Invalid Choice"

print()
print("Simple Calculator:")
print()
a = int (input ("Enter 1st Number: "))
b = int (input ("Enter 2nd Number: "))
print()
print("Choose: + , - , x , / ")
print()
choice = (input ("Enter Choice: "))
print()
s1 = Calculator(a, b)
print(s1.__str__(choice))
print()