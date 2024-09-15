print()
try:
    print()
    x = int (input ("Enter Number 1: "))
    y = int (input ("Enter Number 2: "))
    sum = x / y
except ArithmeticError:
    print()
    print("Arithmetic Error")
else:
    print()
    print(sum)
finally:
    print()
    print("The Code Is Executed.")
print()