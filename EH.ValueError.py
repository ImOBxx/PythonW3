print()
try:
    x = int (input ("Enter Number: "))
except:
    print("The Input Is Not A Valid Integer")
else:
    print(x)
finally:
    print("The Code Is Executed.")
print()