print()
try:
    x = int(input("Enter Numerator: "))
    y = int(input("Enter Denominator: "))
    result = x / y
except:
       print("You cannot divide by zero")
else:
    print(f"The result of {x} divided by {y} is {result}")
finally:
    print("Code Is Executed")
print()