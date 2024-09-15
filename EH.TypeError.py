print()
try:
    x = int (input ("Enter Number 1: "))
    y = int (input ("Enter Number 2: "))
except ValueError as e:
    print(e)
else:
    print(x)
    print(y)
finally:
    print("The Code Is Executed.")
print()